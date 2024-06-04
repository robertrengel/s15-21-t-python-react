from django.db import models
from abstracts.models import AbstractModel
from .constants import (
    PATIENT_GENRE,
    PATIENT_CIVIL_STATUS,
    PATIENT_STATUS,
)
from api.models import ApiUser


# Create your models here.
class UserProfile(AbstractModel):
    user = models.OneToOneField(ApiUser, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=45)
    id_type = models.CharField(max_length=45)
    id_value = models.CharField(max_length=45)
    genre = models.CharField(max_length=3, choices=PATIENT_GENRE)
    civil_status = models.CharField(max_length=1, choices=PATIENT_CIVIL_STATUS)
    birth_date = models.DateField(null=True, blank=True)
    notifications = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=1, choices=PATIENT_STATUS)

    class Meta:
        db_table = "profile"
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.genre
