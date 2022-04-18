from django.contrib import admin
from .models import person
# Register your models here.


class personAdmin(admin.ModelAdmin):
    list_display = ('nom',  'date_creation')


admin.site.register(person, personAdmin)
