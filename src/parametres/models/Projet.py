from django.conf import settings
from django.db import models


class Projet(models.Model):
    # Supprimer l'utilisateur ne supprime pas le projet
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null=True,
    )
    nom = models.CharField(max_length=100)
    date_creation = models.DateField()
    date_modification = models.DateField()