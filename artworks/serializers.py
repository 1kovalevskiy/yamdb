from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import Category, Genre, GenreTitle, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True, required=False)

    class Meta:
        fields = '__all__'
        model = Title

    def create(self, validated_data):
        if 'category' in self.initial_data:
            category = self.initial_data.get('category')
            current_category = get_object_or_404(Category, slug=category)
            title = Title.objects.create(
                **validated_data,
                category=current_category
            )
        else:
            title = Title.objects.create(**validated_data)
        if 'genre' in self.initial_data:
            try:
                genres = self.initial_data.getlist('genre')
            except AttributeError:
                genres = self.initial_data.get('genre')

            for genre in genres:
                current_genre = get_object_or_404(Genre, slug=genre)
                GenreTitle.objects.create(
                    genre=current_genre, title=title)

        return title

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        if 'category' in self.initial_data:
            category = self.initial_data.get('category')
            current_category = get_object_or_404(Category, slug=category)
            instance.category = current_category
            instance.save()
        if 'genre' in self.initial_data:
            try:
                genres = self.initial_data.getlist('genre')
            except AttributeError:
                genres = self.initial_data.get('genre')
            if len(genres) > 0:
                GenreTitle.objects.filter(title=instance).delete()
                for genre in genres:
                    current_genre = get_object_or_404(Genre, slug=genre)
                    GenreTitle.objects.create(
                        genre=current_genre, title=instance)

        return instance
