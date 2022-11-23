from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='scrapper_index'),
    path('scrapp/<int:projet_id>', views.scrapp, name='scrapper_scrapp'),
    path('scrapp/interupt', views.interuptScrapp, name='scrapper_interupt'),
]