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
        "list/",
        medical_history_list,
        name="list",
    ),
]
