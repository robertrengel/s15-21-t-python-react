from django.db import models
from abstracts.models import AbstractModel


# Create your models here.
class Speciality(AbstractModel):
    speciality_name = models.CharField(max_length=50, unique=True)
    speciality_img_url = models.URLField(max_length=120)
    speciality_description = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = "specialities"
        verbose_name = "speciality"
        verbose_name_plural = "specialities"

        def __str__(self):
            return self.speciality_name
