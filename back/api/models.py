from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

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


class CustomUser(models.Model):
    ROLE_CHOICES = (
        ('PAC', 'PACIENTE'),
        ('PRO', 'MEDICO'),
        ('OSA', 'ORGANISMO DE SALUD'),
        ('OAU', 'ORGANISMO DE AUTENTICACION')
        )

    #ISO 3166-1 alfa-3
    COUNTRY_CHOICES = (
        ('ARG', 'ARGENTINA'),
        ('MEX', 'MEXICO'),
        ('PER', 'PERU'),
        ('VEN', 'VENEZUELA')
        )

    user = models.IntegerField() #models.ForeignKey(AbstractBaseUser, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    country_code = models.CharField(choices=COUNTRY_CHOICES, max_length=3)
    uniqueid = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    role_choices = models.CharField(choices=ROLE_CHOICES, default='PAC', max_length=3)