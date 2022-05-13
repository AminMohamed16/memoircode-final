from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

import user

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    # path('logout/',LogoutView.as_view(),name='logout'),
    path('logout/', views.logout_user, name='logout'),

    path('profile/', views.profile, name='profile'),



]
