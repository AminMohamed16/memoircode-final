
from xml.dom.minidom import Document
from django.urls import path
from . import views
from ListEvenment.views import page_Evenment, List_Evenment

urlpatterns = [

    path('', List_Evenment, name="List_Evenment"),
    path('page_Evenment/', page_Evenment, name="page_Evenment"),

]
# /<int:pk>
