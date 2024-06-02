from django.urls import path
from medics_profile.api.v1.viewsets import MedicProfileViewSet

medics_profile_list = MedicProfileViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
medics_profile_detail = MedicProfileViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path(
        "",
        medics_profile_list,
        name="list",
    ),
    path("<int:pk>/", medics_profile_detail, name="medics-profile-detail"),
]
