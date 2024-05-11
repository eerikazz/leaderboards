from django.urls import path
from .views import *

urlpatterns = [
    path('', loginUser, name='loginUser'),
    path('logout/', logoutUser, name='logout'),
    path('<int:user_id>/', fetchUser, name='fetchUser'),
]