from django.urls import path
from medics_profile.api.v1.viewsets import MedicProfileViewSet

medics_profile_list = MedicProfileViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
urlpatterns = [
    path(
        "medics/",
        medics_profile_list,
        name="medics",
    ),
]
