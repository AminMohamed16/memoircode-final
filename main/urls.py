from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
    path('List_Evenment/', include('ListEvenment.urls')),
    path('commendEvent/', include('commendEvent.urls')),
    path('listPerson/', include('person.urls')),



]
