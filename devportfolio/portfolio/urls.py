from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('add-project/', views.add_project, name='add_project'),
]
