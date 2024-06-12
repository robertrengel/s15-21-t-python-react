from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django_countries.fields import CountryField
from django.urls import reverse
from .managers import Doc360UserManager



class Doc360User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
   # name = models.CharField(max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_country = CountryField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    id_nationality = models.IntegerField(default=0)
    date_brith = models.DateField(null=True,blank=True)


    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = Doc360UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("user-detail", kwargs={"pk": self.pk})
