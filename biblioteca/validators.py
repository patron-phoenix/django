
from django.forms import ValidationError


def validar_nombre(value):
    if value=="changos":
        raise ValidationError('%{value}s no es un texto permitido', params={'value':value})