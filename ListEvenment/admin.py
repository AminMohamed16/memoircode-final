from django.contrib import admin
from .models import Evenment
# Register your models here.


class EvenmentAdmin(admin.ModelAdmin):
    list_display = ('nomevenment',  'porte', 'type_evenment','Adresse', 'organisateur','Télephone')

#  , 'Email_Intervenant'

admin.site.register(Evenment, EvenmentAdmin)
