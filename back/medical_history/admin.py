from django.contrib import admin
from .models import MedicalHistory
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

admin.site.register(
    MedicalHistory,
    SimpleHistoryAdmin,
)
