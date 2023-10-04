from django.db import models


class Autor (models.Model):
 
 nombre=models.CharField(max_length=50)
 def __str__(self):
  return self.nombre
 

class Libro(models.Model):
    titulo=models.CharField(max_length=100)
    editorial=models.CharField(max_length=100)
    autor=models.ManyToManyField(Autor)


class Ejemplar(models.Model):
    localizacion=models.CharField(max_length=100)
    libro=models.ForeignKey(Libro,on_delete=models.CASCADE)

    # def __str__(self):
    #     return  self.localizacion, self.libro
    # def __str__(self):
    #     return  self.libro

   

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=10)
    direccion=models.TextField()
    ejemplar=models.ManyToManyField(Ejemplar)


