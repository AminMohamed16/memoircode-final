
from django.urls import path
from . import views

urlpatterns = [

    path('', views.List_Evenment),
    path('/ListEvenment/page_Evenment/', views.page_Evenment),

]
