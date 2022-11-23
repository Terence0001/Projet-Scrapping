from django.urls import path, include
from .views import graphique

urlpatterns = [
    path('', graphique, name="graphique-index"),
]
