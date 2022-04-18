from django.db import models

# Create your models here.


class evenment(models.Model):
    nom_evenment = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'evenment'

    
    def __str__(self):
        return self.country
