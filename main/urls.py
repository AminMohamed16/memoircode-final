from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Accueil.urls')),
    path('List_Evenment/', include('ListEvenment.urls')),


]
