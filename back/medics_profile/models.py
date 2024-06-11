from django.db import models
from api.models import Doc360User
from medics_profile.constants import MEDICS_PROFILE_STATUS
from abstracts.models import AbstractModel


# Create your models here.
class MedicProfile(AbstractModel):
    user = models.ForeignKey(
        Doc360User, on_delete=models.CASCADE, related_name="medics_profile"
    )
    date_of_tuition = models.DateTimeField()
    status = models.CharField(max_length=1, choices=MEDICS_PROFILE_STATUS, default="A")
    observations = models.CharField(max_length=45)
    added_by = models.IntegerField(default=0)

    class Meta:
        db_table = "medics_profile"

        def __str__(self):
            return self.user.username
