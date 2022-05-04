from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
    path('List_Evenment/', include('ListEvenment.urls')),
    path('page_Evenment/', include('ListEvenment.urls')),
    # path('commendEvent/', include('commendEvent.urls')),
    # path('', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)
