from django.urls import path
from .views import register, logIn, logOut

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', logIn, name='login'),
    path('logout/', logOut, name='logout'),
]