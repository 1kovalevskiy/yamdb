from django.conf import settings
from django.contrib import admin

from .models import Category, Genre, GenreTitle, Title


class SiteAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(SiteAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = settings.EMPTY_VALUE


@admin.register(Category)
class CategoryAdmin(SiteAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = settings.EMPTY_VALUE


@admin.register(Title)
class TitleAdmin(SiteAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = settings.EMPTY_VALUE


@admin.register(GenreTitle)
class GenreTitleAdmin(SiteAdmin):
    list_display = ('title_id', 'genre_id',)
    search_fields = ('genre_id',)
    list_filter = ('genre_id',)
    empty_value_display = settings.EMPTY_VALUE
