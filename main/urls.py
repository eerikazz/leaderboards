from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('c/<str:country>', fetchCountry, name='fetchCountry'),
    path('leaderboard', global_leaderboard_view, name='leaderboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)