from django.db import models
from abstracts.models import AbstractModel
#from medical_history.validators import validate_added_by_is_positive_integer
#Querría que me expliques el funcionamiento del validate_name.

# Create your models here.
class Speciality(AbstractModel):
    speciality = models.CharField(max_length=45)
    image_url = models.CharField(max_length=255, default=False, null=False)

    class Meta:
        db_table = "speciality"
        verbose_name = "speciality"
        verbose_name_plural = "specialities"
