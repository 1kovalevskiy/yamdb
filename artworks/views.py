from django.db.models import Avg

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, filters, viewsets
from rest_framework.pagination import PageNumberPagination

from .mixins import CustomViewSet
from .models import Category, Genre, Title
from .permissions import AdminOrReadOnly
from .searches import CustomFilter
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class CategoryViewSet(CustomViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)
    permission_classes = (AdminOrReadOnly, )

    def perform_destroy(self, instance):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                'Необходим JWT-токен!'
            )
        elif self.request.user.role != 'admin':
            raise exceptions.PermissionDenied(
                'Нет прав доступа!'
            )
        super(CategoryViewSet, self).perform_destroy(instance)


class GenreViewSet(CustomViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    search_fields = ('name',)
    permission_classes = (AdminOrReadOnly,)

    def perform_destroy(self, instance):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                'Необходим JWT-токен!'
            )
        elif self.request.user.role != 'admin':
            raise exceptions.PermissionDenied(
                'Нет прав доступа!'
            )
        super(GenreViewSet, self).perform_destroy(instance)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    permission_classes = (AdminOrReadOnly,)
    filterset_class = CustomFilter

    def get_queryset(self):
        return Title.objects.annotate(
            rating=Avg('reviews__score')
        )
