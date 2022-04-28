from django.db import models

# Create your models here.


class person(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    Email = models.CharField(max_length=100, null=True)
    telephon = models.CharField(max_length=100, null=True)
    
def __str__(self):
    return self.nom
