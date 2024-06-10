from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class ApiUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_country = CountryField(blank=True, null=True)
    date_brith = models.DateField(null=True, blank=True)
    id_nationality = models.IntegerField(default=0)


