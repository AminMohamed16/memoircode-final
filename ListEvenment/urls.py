from django.urls import path
from . import views
from .views import Creatnew_evenment,edit_evenment

urlpatterns = [

    path('', views.List_Evenment, name='List_Evenment'),
    path('page_Evenment/<int:id>/', views.page_Evenment, name='page_Evenment'),
    path('mes_evenment/', views.mes_evenment, name='mes_evenment'),
    path('add_evenment/', Creatnew_evenment.as_view(), name='add_evenment'),
    path('page_Evenment/edit/<slug:pk>/', edit_evenment.as_view(), name='edit_Evenment'),
]
