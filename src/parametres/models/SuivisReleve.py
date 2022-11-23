from django.db import models
from .ReleveHistorique import ReleveHistorique

class SuivisReleve(models.Model):
    class Etat(models.IntegerChoices):
        E_C = 1, "EN_COURS"
        T = 2, "TERMINE"
        A = 3, "ANNULE"
    
    # Supprimer un l'historique relevé supprime les threads liés
    rel_historique = models.ForeignKey(ReleveHistorique, on_delete=models.CASCADE)
    etat = models.PositiveSmallIntegerField(
        choices=Etat.choices,
        default=Etat.E_C
    )
    date_debut = models.DateField(auto_now_add=True)
    date_fin = models.DateField(null=True)
    