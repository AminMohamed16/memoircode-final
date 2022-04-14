from django.urls import path
from . import views

urlpatterns = [

    path('', views.sigin),
    # path('', views.login),
    # path('', views.logout),
]
