from django.urls import path
from .views import home_view, aboutMe_view, profile_view

urlpatterns = [
    path('', home_view, name='home'),
    path('/aboutMe', aboutMe_view, name='About Me'),
    path('/profile', profile_view, name='profile'),
]
