from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'artworks'


router_v1 = DefaultRouter()
router_v1.register(r'categories', CategoryViewSet, basename='categories_v1')
router_v1.register(r'genres', GenreViewSet, basename='genres_v1')
router_v1.register(r'titles', TitleViewSet, basename='titles_1')


urlpatterns = [
    path(r'', include(router_v1.urls)),
]
