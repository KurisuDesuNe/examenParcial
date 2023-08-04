from django.urls import path
from . import views

app_name = 'gestionProductos'

urlpatterns = [

    path('', views.index, name='index'),
    path('ejemplo-django', views.ejemplo ,name='ejemplo'),
    path('ejercicio-django', views.ejercicio,name='ejercicio')
    
    

]