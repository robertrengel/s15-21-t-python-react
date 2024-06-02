from django.contrib import admin
from catalogs.models import Speciality


# Register your models here.
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("speciality_name", "speciality_description", "speciality_img_url")
    search_fields = ("speciality_name",)
    list_filter = ("speciality_name",)
    ordering = ("speciality_name",)


admin.site.register(Speciality, SpecialityAdmin)
