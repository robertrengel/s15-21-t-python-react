from django.db import models
from abstracts.models import AbstractModel
from api.models import Doc360User
from catalogs.models import Speciality
from simple_history.models import HistoricalRecords


# Create your models here.
class MedicalHistory(AbstractModel):
    user = models.ForeignKey(
        Doc360User,
        on_delete=models.CASCADE,
        related_name="medical_histories",
    )
    added_by = models.PositiveIntegerField()
    add_datetime = models.DateTimeField()
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    speciality = models.ForeignKey(
        Speciality, on_delete=models.CASCADE, related_name="speciality"
    )
    history = HistoricalRecords()

    class Meta:
        db_table = "medical_histories"
        verbose_name = "medical_history"
        verbose_name_plural = "medical_histories"
