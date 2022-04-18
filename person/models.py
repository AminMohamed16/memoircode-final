from django.db import models

# Create your models here.


class person(models.Model):
    nom = models.CharField(max_length=100, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
