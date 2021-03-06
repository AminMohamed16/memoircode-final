from time import timezone
from django.db import models
from django.utils import timezone
from django.urls import reverse

# from map.models import Data
# from distutils.command.upload import upload
# from user.models import User
# Evenment_list MODEL


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
    # country = models.CharField(max_length=100, null=True)
    # ville = models.ForeignKey(Data,on_delete=models.CASCADE)
    porte = models.CharField(max_length=100, null=True,
                             choices=TypeIntervenant)
    type_evenment = models.CharField(
        max_length=100, null=True, choices=TYPE_EVENMENT)
    Adresse_deEvent = models.CharField(max_length=100, null=True)
    # Télephone = models.CharField(max_length=100, null=True)
    Email_Intervenant = models.CharField(max_length=100, null=True)
    organisateur = models.CharField(
        max_length=100, null=True, choices=organisateur)
    Descriptinos = models.TextField(null=True)
    date_creation_evenment = models.DateTimeField(default=timezone.now)
    date_fine_evenment = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = ("Evenment")
        verbose_name_plural = ("Evenment")
        ordering = ('-date_creation_evenment',)

    def __str__(self):
        return self.nomevenment

    def get_absolute_url(self):
        # return reverse('page_Evenment', args=(str(self.id)))
        return reverse('List_Evenment')
