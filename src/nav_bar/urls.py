from django.urls import path, include
from .views import nav_bar

urlpatterns = [
    path('', nav_bar, name="nav_bar-index"),
]
from django.urls import path, include
from .views import nav_bar

urlpatterns = [
    path('', nav_bar, name="nav_bar-index"),
]
