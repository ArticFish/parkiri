from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

from .models import estacionamiento, estadoc, estadoe, tipoc
User = get_user_model()
# Create your views here.

def inicio(request):
    return render(request,'index.html')

def mapa(request):
    return render(request,'mapa.html')

def aestacionamiento(request):
    return render(request,'agregar.html')

def editestacionamiento(request,ide):
    lista = estacionamiento.objects.get(estacionamiento=ide)
    contexto={"listae":lista}
    return render(request,'editar.html',contexto)

def eestacionamiento(request,ide):
    ubi = request.POST['ubicacion']
    prec = request.POST['precio']
    fotoe = request.FILES['subir']
    esta=estacionamiento.objects.get(estacionamiento=ide)
    esta.direccion = ubi
    esta.precio = prec
    esta.foto = fotoe
    esta.save()
    print('Funciono correctamente')
    return redirect('perfil')

def deshabilitare(request,ide):
    est = estadoe
    est.estado = estadoe.objects.get(nombre='Deshabilitado')
    estaciona=estacionamiento.objects.get(estacionamiento=ide)
    estaciona.estado = est.estado
    estaciona.save()
    return redirect('perfil')

def habilitare(request,ide):
    est = estadoe
    est.estado = estadoe.objects.get(nombre='Habilitado')
    estaciona=estacionamiento.objects.get(estacionamiento=ide)
    estaciona.estado = est.estado
    estaciona.save()
    return redirect('perfil')

def aceptare(request,ide):
    est = estadoe
    est.estado = estadoe.objects.get(nombre='Habilitado')
    estaciona=estacionamiento.objects.get(estacionamiento=ide)
    estaciona.estado = est.estado
    estaciona.save()
    return redirect('perfil')

def rechazare(request,ide):
    est = estadoe
    est.estado = estadoe.objects.get(nombre='Rechazado')
    estaciona=estacionamiento.objects.get(estacionamiento=ide)
    estaciona.estado = est.estado
    estaciona.save()
    return redirect('perfil')

def eliminare(request,ide):
    estaciona=estacionamiento.objects.get(estacionamiento=ide)
    estaciona.delete()
    return redirect('perfil')

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
        return redirect('inicio')
    else:
        messages.success(request,'Usuario o contrasena incorrectos')
        return redirect('prueba')

def registro(request):
    nombre = request.POST['registrarUser']
    clave = request.POST['registrarContra']
    correo = request.POST['registrarCorreo']
    ru = request.POST['rut']
    dire = request.POST['direccion']
    tele = request.POST['telefono']
    try:
        c = request.POST['registrarRol']
        cuenta = tipoc.objects.get(tipoc=c)
        tip = tipoc
        tip.tipoc = cuenta
    except:
        c = request.POST['registrarRol']
        cuenta = tipoc.objects.get(tipoc=c)
        tip = tipoc
        tip.tipoc = cuenta
        
    user = User.objects.create_user(nombre, correo, clave,rut=ru,direccion=dire,telefono=tele,tipo=tip.tipoc)
    user.save()
    print(cuenta.tipoc)
    print('Funciono correctamente')
    return redirect('prueba')

def eperfil(request,idu):
    user = User.objects.get(id=idu)
    nombre = request.POST['registrarUser']
    clave = request.POST['registrarContra']
    correo = request.POST['registrarCorreo']
    dire = request.POST['registrarDireccion']
    tele = request.POST['registrarTelefono']
    if clave == '':
        print('xd')
    else:
        user.set_password(clave)
    user.username = nombre
    user.email=correo
    user.direccion= dire
    user.telefono = tele
    user.save()
    return redirect('inicio')

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


