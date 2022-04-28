
from django.db import models
from person.models import person
from ListEvenment.models import Evenment
from map.models import Data

# from map.models import Data
# Create your models here.


class list_CommandEvent(models.Model):
    TypeIntervenant = (
        ('national', 'national'),
        ('international', 'international'),
        ('wilaya', 'wilaya'),
        ('interwilaya', 'interwilaya')
    )
    porte = models.CharField(max_length=100, null=True,choices=TypeIntervenant)
    person=models.ForeignKey(person,null=True,on_delete=models.SET_NULL)
    ListEvenment=models.ForeignKey(Evenment,null=True,on_delete=models.SET_NULL)
    map=models.ForeignKey(Data,null=True,on_delete=models.SET_NULL)

    


    def __str__(self):
        return self.porte
