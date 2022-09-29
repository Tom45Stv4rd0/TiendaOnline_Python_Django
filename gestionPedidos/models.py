from django.db import models
from django.db.models.fields import CharField 

# Create your models here.

class cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=80)
    mail=models.EmailField()
    tfono=models.CharField(max_length=9)
    tfono_fijo=models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return 'el nombre del cliente es %s su direccion es %s e-mail es %s y telefono es %s'%(self.nombre, self.direccion, self.mail, self.tfono)

class articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=80)
    precio=models.IntegerField()


class pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()