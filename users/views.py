from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .permissions import IsAdmin
from .serializers import (AccessTokenObtainSerializer,
                          UserCreateWithEmailSerializer, UserSerializer)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def user_create_with_email(request):
    serializer = UserCreateWithEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data.get('username')
    if user == 'me':
        raise ValidationError(
            'Unable to get or create user '
            'with given attributes.'
        )

    try:
        user, created = User.objects.get_or_create(
            email=serializer.data['email'],
            username=serializer.data['username'],
        )
    except (IntegrityError, User.DoesNotExist):
        raise ValidationError(
            'Unable to get or create user '
            'with given attributes.'
        )

    if created:
        user.set_unusable_password()
        user.save()

    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'YaMDb: get your confirmation code!',
        (
            f'Hi, {user.username}! Use the code below '
            'to get access token: \n'
            f'{confirmation_code}'
        ),
        None,
        (user.email,),
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def access_token_obtain(request):
    serializer = AccessTokenObtainSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = get_object_or_404(
        User,
        username=serializer.data['username'],
    )

    if not default_token_generator.check_token(
            user,
            serializer.data['confirmation_code'],
    ):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    access = AccessToken.for_user(user)
    data = {
        'token': str(access),
    }
    return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(None))

    @action(
        methods=('GET', 'PATCH'),
        detail=False,
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request, **kwargs):
        user = request.user

        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(role=user.role)
        return Response(serializer.data, status=status.HTTP_200_OK)
