from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),
    path('profile/', views.profile, name='users-profile'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', views.LogoutView.as_view(), name='users-logout'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    
]