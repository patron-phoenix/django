from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Autor,Libro,Ejemplar,Usuario
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import AutorSerializer, LibroSerializer, EjemplarSerializer,UsuarioSerializer

# def index(request):
#     return HttpResponse("HOLA CHANGOS")

# def autor(request):
#     return HttpResponse("bienvenido a autores")

#Autor ModelViewSet

class AutorViewSet(viewsets.ModelViewSet):
    queryset=Autor.objects.all()
    serializer_class=AutorSerializer


#Libro ModelViewSet

class LibroViewSet (viewsets.ModelViewSet):
    queryset=Libro.objects.all()
    serializer_class=LibroSerializer

#ejemplar ModelViewSet

class EjemplarViewSet (viewsets.ModelViewSet):
    queryset=Ejemplar.objects.all()
    serializer_class=EjemplarSerializer

#usuario ModelViewSet

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer


#api custom

@api_view(["GET"])
def autores_count(request):
    """
    Cantidad de Autores 
    """
    try:
        cantidad=Autor.objects.count()
        return JsonResponse(
            {"cantidad": cantidad},
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, safe=False,status=500)