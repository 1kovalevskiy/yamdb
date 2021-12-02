from django.shortcuts import get_object_or_404

from rest_framework import exceptions, serializers

from .models import Comment, Review

from artworks.models import Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        exclude = ('title',)
        model = Review

    def validate(self, attrs):
        request = self.context.get('request')
        if not request.method == 'POST':
            return attrs

        title_id = request.parser_context['kwargs']['title_id']
        title = get_object_or_404(Title, id=title_id)
        if not request.user.is_authenticated:
            raise exceptions.AuthenticationFailed
        if title.reviews.filter(author=request.user).exists():
            raise serializers.ValidationError(
                'You reviewed this title already'
            )
        return attrs


class ReviewGetSerializer(serializers.ModelSerializer):
    results = ReviewSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        exclude = ('review',)
        model = Comment

    def validate(self, attrs):
        request = self.context.get('request')
        if not request.method == 'POST':
            return attrs

        if not request.user.is_authenticated:
            raise exceptions.AuthenticationFailed
        return attrs
