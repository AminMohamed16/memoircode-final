from django.contrib import admin
from .models import list_CommandEvent
# Register your models here.


class CommandEvent(admin.ModelAdmin):
    list_display = ('porte', 'map', 'person', 'ListEvenment')
# ,'map'


admin.site.register(list_CommandEvent, CommandEvent)
