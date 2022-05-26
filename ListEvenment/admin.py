from django.contrib import admin
from .models import Evenment
# from .views import Creatnew_evenment
# Register your models here.


class EvenmentAdmin(admin.ModelAdmin):
    list_display = ('nomevenment', 'image', 'Acountry', 'Descriptinos', 'date_fine_evenment',
                    'date_creation_evenment', 'porte', 'type_evenment', 'Adresse_deEvent',
                    'organisateur', 'Email_Intervenant')

#  , 'Email_Intervenant'


admin.site.register(Evenment, EvenmentAdmin)
# admin.site.register(Creatnew_evenment, Creatnew_evenment)
