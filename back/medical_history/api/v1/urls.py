from django.urls import path
from medical_history.api.v1.viewsets import MedicalHistoryViewSet

medical_history_list = MedicalHistoryViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

urlpatterns = [
    path(
        "patients",
        medical_history_list,
        name="patients",
    ),
]
