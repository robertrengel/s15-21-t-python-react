from django.db import models
from medical_history.models import MedicalHistory
from api.models import ApiUser

# Create your models here.

class Comment(models.Model):
    history_id = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, )
    user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"
        verbose_name = "comments"
        verbose_name_plural = "comments"

    def __str__(self):
        return self.comment
