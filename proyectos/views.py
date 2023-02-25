from django.shortcuts import render, redirect
from .models import Proyecto, Contacto

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

def addContact(request):
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    email = request.POST['email']
    mensaje = request.POST['mensaje']
    
    contacto = Contacto.objects.create(
        nombre = nombre,
        telefono = telefono,
        email = email,
        mensaje = mensaje)
    
    return redirect('/')