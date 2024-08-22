from django.db import models

# Create your models here.


class Challenge(models.Model):
    mois = models.CharField(max_length=10)
    titre = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):          # me retourne le mois d'un challenges specifique
        return self.mois
