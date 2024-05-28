from django.db import models
from abstracts.models import AbstractModel
from django.contrib.auth.models import User
from medical_history.validators import validate_added_by_is_positive_integer


# Create your models here.
class MedicalHistory(AbstractModel):
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name="medical_histories",
    # )
    added_by = models.PositiveIntegerField()
    add_datetime = models.DateTimeField()
    speciality = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    class Meta:
        db_table = "medical_histories"
        verbose_name = "medical_history"
        verbose_name_plural = "medical_histories"
