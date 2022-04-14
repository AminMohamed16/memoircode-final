from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Accueil.urls')),
    path('List_Evenment/', include('List_Evenment.urls')),
    path('sigin/', include('sigin.urls')),
    # path('login/', include('login.urls')),
    # path('Sigin/', include('logout.urls')),

]
