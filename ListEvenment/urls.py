
from django.urls import path
from . import views
# from .views import Creatnew_evenment
# from ListEvenment.views import page_Evenment, List_Evenment
urlpatterns = [

    path('', views.List_Evenment, name='List_Evenment'),
    path('page_Evenment/<int:id>/', views.page_Evenment, name='page_Evenment'),
    path('mes_evenment/', views.mes_evenment, name='mes_evenment'),
    # path('new_evenment/', Creatnew_evenment.as_view(), name='Creatnew_evenment'),

]
