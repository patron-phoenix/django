
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('biblioteca/',include("biblioteca.urls")),
]

get_schema_view = get_schema_view(
    openapi.Info(
        title="Curso django",
        default_version="v1",
        description="Curso de Django",
        terms_of_service="http",
        contact=openapi.Contact(email="patron.phoenix@gmail.com"),
        license=openapi.License(name="ISCH License"),
    ),
    public= True,
    permission_classes=[permissions.AllowAny,],
)

# if settings.DEBUG:
#     urlpatterns +=[
#         re_path(
#             r"^apidoc(?P<format>\.json|\.yaml)$",
#             schema_view.without_ui(cache_timeout=0),
#             name="schema-json",
#         ),
#         re_path(
#             r"^apidoc/$",
#             schema_view.without_ui("swagger", cache_timeout=0),
#             name="schema-swagger-ui",
#         ),
#     ]