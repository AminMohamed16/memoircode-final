from typing import List
from django.db import models
from person.models import person
from ListEvenment.models import Evenment

import geocoder

# Create your models here.


class Data(models.Model):
    country = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    person=models.ForeignKey(person,null=True,on_delete=models.SET_NULL)
    ListEvenment=models.ForeignKey(Evenment,null=True,on_delete=models.SET_NULL)



    class Meta:
        verbose_name_plural = 'Data'

    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.country).lat
        self.longitude = geocoder.osm(self.country).lng
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.country
