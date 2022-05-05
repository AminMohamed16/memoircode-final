from time import timezone
from django.db import models
from django.utils import timezone
# Create your models here.
from distutils.command.upload import upload

# Create your models here.

# Evenment_list MODEL
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
    date_creation_evenment = models.DateTimeField(default=timezone.now)
    date_fine_evenment = models.DateTimeField(default=timezone.now)
    image=models.ImageField(blank=True,null=True)
    class Meta:
        verbose_name = ("Evenment")
        verbose_name_plural = ("Evenment")
        ordering=('-date_creation_evenment',)
    def __str__(self):
        return self.nomevenment


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField(max_length=50)
    Comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    Evenment = models.ForeignKey(Evenment, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return ' {} Comment for :{}.'.format(self.name,self.Evenment)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comment")
        ordering=('-Comment_date',)