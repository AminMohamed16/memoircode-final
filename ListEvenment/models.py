
from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Evenment(models.Model):

    organisateur = (
        ('SARL', 'SARL'),
        ('EURL', 'EURL'),
        ('AMBASSADE', 'AMBASSADE'),
        ('ASSOCIATION', 'ASSOCIATION'),
        ('FEDERATION', 'FEDERATION'),
        ('MINISTERE', 'MINISTERE'),
        ('ARTISAN', 'ARTISAN'),
        ('CHAMBRE', 'CHAMBRE'),
        ('SPA', 'SPA')
    )
    TypeIntervenant = (
        ('national', 'national'),
        ('international', 'international'),
        ('wilaya', 'wilaya'),
        ('interwilaya', 'interwilaya')
    )
    TYPE_EVENMENT = (
        ('culturel', 'culturel'),
        ('sport', 'sport'),
        ('religieux', 'religieux'),
        ('scientifiques', 'scientifiques')
    )

    nomevenment = models.CharField(max_length=100, null=True)
    country=models.CharField(max_length=100, null=True)
    porte = models.CharField(max_length=100, null=True,choices=TypeIntervenant)
    type_evenment = models.CharField(max_length=100, null=True, choices=TYPE_EVENMENT)
    Adresse_deEvent = models.CharField(max_length=100, null=True)
    # Télephone = models.CharField(max_length=100, null=True)
    Email_Intervenant=models.CharField(max_length=100, null=True)
    organisateur = models.CharField(max_length=100, null=True, choices=organisateur)
    Descriptinos = models.TextField(null=True)
    date_creation = models.DateTimeField(null=True)
    # image=models.ImageField(upload_to='brand_img/')

    def __str__(self):
        return self.nomevenment
