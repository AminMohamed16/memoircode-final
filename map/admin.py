from django.contrib import admin
from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('country','person', 'latitude', 'longitude','ListEvenment')


admin.site.register(Data, DataAdmin)
