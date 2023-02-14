from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def landing(request):
    template_to_return='hola.html'
    formulario=pastelform()
    consulta=pastel.objects.all()

    context={
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request, template_to_return, context)