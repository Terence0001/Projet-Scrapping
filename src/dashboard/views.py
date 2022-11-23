from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from parametres.models import ReleveHistorique, Projet
from django.db.models import Count
from django.db.models import Max
from django.urls import reverse



def index(request):
    return render(request, "dashboard.html")


def index(request):
  projetEnCours = ReleveHistorique.objects.values('projet_id').annotate(total=Count('id'),latest_date=Max('date_rel'))
  template = loader.get_template('dashboard.html')
  context = {
    'projetEnCours': projetEnCours,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add_project.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['nom']
  y = request.POST['date_creation']
  z = request.POST['date_modification']
  project = Projet(nom=x,date_creation=y,date_modification=z)
  project.save()
  return HttpResponseRedirect(reverse('dashboard_index'))

def delete(request, projet_id):
  project = Projet.objects.get(id=projet_id)
  project.delete()
  return HttpResponseRedirect(reverse('dashboard_index'))

def update(request, projet_id):
  project = Projet.objects.get(id=projet_id)
  template = loader.get_template('update_project.html')
  context = {
    'project': project,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, projet_id):
  nom = request.POST['nom']
  #date_creation = request.POST['date_creation']
  #date_modification = request.POST['date_modification']
  project = Projet.objects.get(id=projet_id)
  project.nom = nom
  #project.date_creation = date_creation
  #project.date_modification = date_modification

  project.save()
  return HttpResponseRedirect(reverse('dashboard_index'))
