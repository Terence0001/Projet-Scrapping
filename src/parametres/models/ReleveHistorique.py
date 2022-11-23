from django.db import models
from .Projet import Projet
from django.conf import settings

class ReleveHistorique(models.Model):
    # Supprimer un projet ne supprime pas l'historique de relevé
    id = models.AutoField(primary_key=True)
    projet = models.ForeignKey(Projet, on_delete=models.SET_NULL, null=True)

    date_rel = models.DateField(auto_now_add=True)
    etat_rel = models.BooleanField(default=False)
    nb_nouveau_threads = models.IntegerField(null=True)
    #nb_thread = models.IntegerField()

    
    def nb_thread_rel(self):
        return self.objects.select_related("thread").count()
    
    def nb_comm_rel(self):
        return self.objects.select_related("thread", "commentaire").filter(thread__releve_istorique=self.id).count()

