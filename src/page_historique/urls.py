from django.urls import path, include
from .views import pageHistorique

urlpatterns = [
    path('', pageHistorique, name="pageHistorique-index"),
]
