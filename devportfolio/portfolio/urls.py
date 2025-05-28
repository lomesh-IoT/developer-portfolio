from django.urls import path
from .views import register_view, profile_view, home_view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('projects/', views.project_list_view, name='project_list'),
    path('projects/add/', views.add_project_view, name='add_project'),
]