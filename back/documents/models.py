from django.db import models
from abstracts.models import AbstractModel
from api.models import ApiUser
from medical_history.models import MedicalHistory
#from catalogs.models import Speciality


# Create your models here.
class Documents(AbstractModel):
    owner = models.ForeignKey(
        ApiUser,
        on_delete=models.PROTECT,
        related_name="documents",
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    filename = models.CharField(max_length=100, null=False, blank=False)
    file_path = models.CharField(max_length=100, null=False, blank=False)
    medical_history = models.ForeignKey(
        MedicalHistory, 
        on_delete=models.CASCADE, 
        related_name="medical_histories"
    )

    class Meta:
        db_table = "documents"
        verbose_name = "document"
        verbose_name_plural = "documents"
