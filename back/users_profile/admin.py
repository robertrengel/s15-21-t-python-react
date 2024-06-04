from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "civil_status",
        "status",
    )
    search_fields = ("status",)
    ordering = ("user_id",)


admin.site.register(UserProfile, ProfileAdmin)
