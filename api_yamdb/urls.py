from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/', include('artworks.urls', namespace='artworks')),
    path('api/v1/', include('users.urls', namespace='authentication')),
    path('api/v1/', include('reviews.urls', namespace='reviews')),

]
