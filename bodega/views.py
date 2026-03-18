# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def bodega(request):
    # Por ahora, solo mandamos un texto simple para probar
    return HttpResponse("<h1>¡Hola! Estás en el panel de la Bodega</h1>")