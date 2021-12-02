from django.conf import settings
from django.contrib import admin

from .models import Review


class SiteAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(SiteAdmin):
    list_display = ('title', 'text', 'author', 'score', 'pub_date')
    search_fields = ('title', 'author')
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY_VALUE
