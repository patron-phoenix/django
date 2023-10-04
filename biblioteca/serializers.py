from rest_framework import serializers
from .models import Autor,Libro, Ejemplar,Usuario
from .validators import validar_nombre

#Autor
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autor
        fields='__all__'

#Libro
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields='__all__'

#Ejemplar
class EjemplarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ejemplar
        fields='__all__'

#Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'