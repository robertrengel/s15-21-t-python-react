from django.db import models
from django.utils import timezone

"""
class Country(models.Model):
    #ISO 3166-1 alfa-3
    iso3 = models.CharField(max_length=3, unique=True)
    isonum = models.CharField(max_length=3, unique=True)
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class Role(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')

"""


class ApiUser(models.Model):
    ROLE_CHOICES = (
        ("PAC", "PACIENTE"),
        ("MED", "MEDICO"),
        ("OSA", "ORGANISMO DE SALUD"),
        ("OAU", "ORGANISMO DE AUTENTICACION"),
    )

    # ISO 3166-1 alfa-3
    COUNTRY_CHOICES = (
        ("ARG", "ARGENTINA"),
        ("MEX", "MEXICO"),
        ("PER", "PERU"),
        ("VEN", "VENEZUELA"),
    )

    STATUS_CHOICES = (("P", "PENDIENTE"), ("A", "ACTIVO"), ("I", "INACTIVO"))

    uniqueid = models.CharField(max_length=50, unique=True)
    country_code = models.CharField(choices=COUNTRY_CHOICES, max_length=3)
    role = models.CharField(choices=ROLE_CHOICES, default="PAC", max_length=3)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    id_type = models.CharField(max_length=255, default="")
    id_value = models.CharField(max_length=255, default="")
    genre = models.CharField(max_length=255, default="")
    civil_status = models.CharField(max_length=255, default="")
    birth_date = models.DateField(null=True, editable=False)
    password = models.CharField(max_length=255)
    created_by = models.CharField(max_length=50, default="Usuario", null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    notifications = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default="P")
