from django.urls import path
from . import views

app_name = 'gestionTiendas'

urlpatterns = [

    path('inicio', views.index, name='index'),
    path('ejemplo-django', views.ejemplo ,name='ejemplo'),
    path('ejercicio-django', views.ejercicio,name='ejercicio'),
    path('PanelProductos', views.PanelProductos,name='PanelProductos'),
    path('PanelTienda', views.PanelTienda,name='PanelTienda')

]