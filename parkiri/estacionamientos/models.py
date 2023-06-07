from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class tipoc(models.Model):
    tipoc = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del tipo de cuenta")
    tipo = models.CharField(max_length=50, verbose_name="tipo",blank=False,null=False)

    def __str__(self):
        return self.tipo

class estadoc(models.Model):
    estado = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del estado cuenta")
    tipo = models.CharField(max_length=50, verbose_name="tipo",blank=False,null=False)

    def __str__(self):
        return self.tipo

class estadoe(models.Model):
    estado = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del estado estacionamiento")
    nombre = models.CharField(max_length=50, verbose_name="tipo",blank=False,null=False)

    def __str__(self):
        return self.nombre
    

class UserProfile(AbstractUser):
    estado = models.ForeignKey(estadoc,on_delete=models.CASCADE,default=1)
    tipo = models.ForeignKey(tipoc,on_delete=models.CASCADE,default=1)

class estacionamiento(models.Model):
    estacionamiento = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del estacionamiento")
    direccion = models.CharField(max_length=200, verbose_name="tipo",blank=False,null=False)
    precio = models.IntegerField(verbose_name="Precio estacionamiento")
    estado = models.ForeignKey(estadoe,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.estacionamiento)
    
class reserva(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=1)
    estacionamiento = models.ForeignKey(estacionamiento,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.user