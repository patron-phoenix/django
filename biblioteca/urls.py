from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"autores",views.AutorViewSet)
router.register(r"libros",views.LibroViewSet)
router.register(r"ejemplares",views.EjemplarViewSet)
router.register(r"usuarios",views.UsuarioViewSet)

urlpatterns = [
    #path("",views.index,name="index"),
    path("", include(router.urls)),
    path("aut/cantidad/",views.autores_count,name="autores_count")
    #path("autor/",views.autor,name="autor")
]
