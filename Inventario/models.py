# Create your models here.
from django.db import models
from Tsukuyomi.fields import NullCharField


class Edificio(models.Model):
    nombre = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nombre


class Aula(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    edificio = models.ForeignKey(Edificio)

    def __str__(self):
        return '{}/{}'.format(self.edificio, self.nombre)


class Marca(models.Model):
    nombre = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nombre


class Material(models.Model):
    codigo_interno = models.CharField(unique=True, max_length=15)
    codigo_utez = NullCharField(unique=True, blank=True, null=True, max_length=15)
    codigo_vendedor = NullCharField(unique=True, blank=True, null=True, max_length=15)
    ubicacion = models.ForeignKey(Aula)
    marca = models.ForeignKey(Marca)
    cantidad = models.PositiveIntegerField(default=1)
    tipo = models.ForeignKey(Tipo)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return '{}/{}/{} - {}/{}'.format(self.codigo_interno,
                                         self.codigo_utez or 'NA',
                                         self.codigo_vendedor or 'NA',
                                         self.tipo,
                                         self.marca)