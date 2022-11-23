from django.db import models
from .Thread import Thread

class Commentaire(models.Model):
    # Supprimer un thread supprime les commentaires liés
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)