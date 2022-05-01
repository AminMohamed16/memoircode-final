from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_visiteur = models.BinaryField(null=True)
    is_utilisateur = models.BinaryField(null=True)
    is_utilisateur_agrre = models.BinaryField(null=True)
