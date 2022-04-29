from django.contrib import admin
from .models import Evenment
# Register your models here.


class EvenmentAdmin(admin.ModelAdmin):
    list_display = ('nomevenment','image','country', 'Descriptinos', 'date_creation', 'porte',
                    'type_evenment', 'Adresse_deEvent', 'organisateur', 'Email_Intervenant')

#  , 'Email_Intervenant'


admin.site.register(Evenment, EvenmentAdmin)
