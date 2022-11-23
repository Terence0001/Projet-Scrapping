from django.urls import path
from . import views

urlpatterns = [
    path('<int:projet_id>', views.index, name='project_index'),
]