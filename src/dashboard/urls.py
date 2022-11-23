from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:projet_id>', views.delete, name='delete'),
    path('update/<int:projet_id>', views.update, name='update'),
    path('update/updaterecord/<int:projet_id>', views.updaterecord, name='updaterecord'),
]