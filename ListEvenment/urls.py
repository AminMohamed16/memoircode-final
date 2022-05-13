
from django.urls import path
from . import views
# from ListEvenment.views import page_Evenment, List_Evenment

urlpatterns = [

    path('', views.List_Evenment, name='List_Evenment'),
    path('page_Evenment/<int:id>/', views.page_Evenment, name='page_Evenment'),
    path('mes_evenment/', views.mes_evenment, name='mes_evenment'),

]
