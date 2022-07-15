from django.db import models

# Create your models here.


#-----Cliente-----#
class Genero (models.Model):
    idGenero = models.IntegerField(primary_key=True, verbose_name='Id de Genero')
    nombreGenero = models.CharField(max_length=50, verbose_name='Nombre de Genero')

    def __str__(self):
        return self.nombreGenero

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    correo = models.CharField(max_length=30, verbose_name='Correo' )
    telefono = models.CharField( max_length=11, verbose_name='Telefono' )
    direccion = models.CharField(max_length=65, verbose_name='Direccion')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name='Genero')

    def __str__(self):
        return self.rut

#-----Producto-----#

class Tamanio (models.Model):
    idTamanio = models.IntegerField(primary_key=True, verbose_name='Id de Tamaño')
    nombreTamanio = models.CharField(max_length=50, verbose_name='Nombre de Tamaño')

    def __str__(self):
        return self.nombreTamanio

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, verbose_name='Codigo')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    precio = models.IntegerField( verbose_name='Precio')
    tamanio = models.ForeignKey(Tamanio, on_delete=models.CASCADE, verbose_name='Tamaño')
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.codigo