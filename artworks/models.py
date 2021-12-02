from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='genre-name')
    slug = models.SlugField(unique=True,
                            verbose_name='genre-slug')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='category-name')
    slug = models.SlugField(unique=True,
                            verbose_name='category-slug')

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='title-name')
    year = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(
            datetime.now().year,
            message=('Вы пытаетесь внести '
                     'еще не вышедшее произведение')),),
        verbose_name='title-year',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='title',
        verbose_name='title-category',
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(Genre,
                                   through='GenreTitle',
                                   verbose_name='title-genre')
    description = models.TextField(blank=True,
                                   verbose_name='title-description')

    class Meta:
        ordering = ('-year',)

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='genre-title')
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='genre')

    def __str__(self):
        return (self.title_id.name[:15] + '-->' + self.genre_id.name[:15])

    def __repr__(self):
        return (self.title_id.name[:15] + '-->' + self.genre_id.name[:15])
