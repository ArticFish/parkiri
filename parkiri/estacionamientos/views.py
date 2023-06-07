from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

from .models import estacionamiento, estadoe
User = get_user_model()
# Create your views here.

def inicio(request):
    return render(request,'index.html')

def mapa(request):
    return render(request,'mapa.html')

def aestacionamiento(request):
    return render(request,'agregar.html')

def editestacionamiento(request):
    return render(request,'editestacionamiento.html')

def agregarestacionamiento(request):
    ubi = request.POST['ubicacion']
    prec = request.POST['precio']
    fotoe = request.FILES['subir']
    estacionamiento.objects.create(direccion=ubi,precio=prec,foto=fotoe)
    print('Funciono correctamente')
    return redirect('perfil')

def reset_password(request):
    return render(request,'registration/password_reset.html')

def registrarse(request):
    return render(request,'registrarse.html')

def perfil(request):
    listae=estacionamiento.objects.all()
    contexto = {'lista':listae}
    return render(request,'perfil.html',contexto)

def recuperarContrasena(request):
    return render(request,'recuperarContrasena.html')

def prueba(request):
    user = User.objects.all()
    contexto={"usuario":user}
    return render(request,'prueba.html',contexto)

def cerrarsesion(request):
    logout(request)
    return render(request,'index.html')

def iniciarsesion(request):
    user = request.POST['username']
    contra= request.POST['contra']
    user = authenticate(username=user, password=contra)
    if user is not None:
        login(request, user)
        messages.success(request,'Usuario autenticado')
        return render(request,'index.html')
    else:
        messages.success(request,'Usuario o contrasena incorrectos')
        return render(request,'prueba.html')

def registro(request):
    nombre = request.POST['registrarUser']
    clave = request.POST['registrarContra']
    correo = request.POST['registrarCorreo']
    
    try:
        user = User.objects.create_user(nombre, correo, clave)
        user.save()
        print('Funciono correctamente')
        return render(request,'prueba.html')
    except:
        print('Dio un error')
        return render(request,'registrarse.html')

def ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse("Welcome! You are visiting from: {}".format(ip))

def enviar_correo(request):
    print("bien")
    if request.method == 'POST':
        destinatario = request.POST['destinatario']
        subject = 'Correo de prueba'
        message = 'Este es un correo de prueba enviado desde Django.'
        from_email = 'sergio.onep@gmail.com'
        to_email = [destinatario]
        print("bien2")
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        print("bien22")
        return render(request, 'index.html')


