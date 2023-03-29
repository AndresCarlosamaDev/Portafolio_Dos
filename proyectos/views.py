from django.shortcuts import render, redirect
from .models import Proyecto, Contacto
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

def addContact(request):
    try:
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        
        contacto = Contacto.objects.create(
            nombre = nombre,
            telefono = telefono,
            email = email,
            mensaje = mensaje)
        
        asunto = request.POST['nombre'] + ' ' + request.POST['telefono'] + ' ' + request.POST['email']
        mensaje = request.POST['mensaje']
        email_desde = settings.EMAIL_HOST_USER
        email_para = ['andrescarlosdev@gmail.com']
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, 'emailSuccessfully.html', {})
    except:
        return render(request, 'emailFail.html', {})