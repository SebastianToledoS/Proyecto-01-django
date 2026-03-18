from django.urls import path
from . import views  # Importa el cerebro de la bodega

urlpatterns = [
    # Cuando la URL sea 'bodega/', ejecuta la función 'index'
    path('', views.bodega, name='bodega'),
]