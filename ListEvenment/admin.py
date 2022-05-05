from django.contrib import admin
from .models import Evenment,Comment
# Register your models here.


class EvenmentAdmin(admin.ModelAdmin):
    list_display = ('nomevenment', 'image', 'country', 'Descriptinos', 'date_fine_evenment', 'date_creation_evenment', 'porte',
                    'type_evenment', 'Adresse_deEvent', 'organisateur', 'Email_Intervenant')

#  , 'Email_Intervenant'


admin.site.register(Evenment, EvenmentAdmin)

admin.site.register(Comment)
