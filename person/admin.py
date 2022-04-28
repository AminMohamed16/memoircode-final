from django.contrib import admin
from .models import person
# Register your models here.


class personAdmin(admin.ModelAdmin):
    list_display = ('nom',  'prenom', 'Email', 'telephon')


admin.site.register(person, personAdmin)
