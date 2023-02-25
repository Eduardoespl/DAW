from django.shortcuts import render
from .forms import *
from .models import *
from multiprocessing import context
from django.shortcuts import redirect

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

def post_pastel(request):
    if request.method == 'POST':
        form = pastelform(request.POST, request.FILES)
        if form.is_valid():
            pastel.objects.create(
                cubierta=request.POST['cubierta'],
                precio=request.POST['precio'],
                sabor=request.POST['sabor'],
                peso=request.POST['peso'],
                pisos=request.POST['pisos'],
                tipo=request.POST['tipo'],            
            )
            return redirect('landing')
        else:
            form = pastelform( )
        return render(request, 'hola.html', context)
    