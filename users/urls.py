from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, access_token_obtain, user_create_with_email

app_name = 'authentication'

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path(r'', include(router_v1.urls)),
    path('auth/signup/', user_create_with_email, name='user-create'),
    path('auth/token/', access_token_obtain, name='token_obtain'),
]
