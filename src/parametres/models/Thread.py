from django.db import models
from .ReleveHistorique import ReleveHistorique

class Thread(models.Model):
    # Supprimer un l'historique relevé supprime les threads liés
    rel_historique = models.ForeignKey(ReleveHistorique, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)