from django.shortcuts import render
from parametres.models import Projet

def index(request, projet_id):
    projet = Projet().__class__.objects.get(id=projet_id)

    return render(request, "project.html", {
            "nom_projet": projet.nom,
    })