# practica_05/views.py
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    context["user"] = "migue"
    return render(request,'basico.html', context)
