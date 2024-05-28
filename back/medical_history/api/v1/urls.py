from django.urls import path
from rest_framework.routers import DefaultRouter
from medical_history.api.v1.viewsets import MedicalHistoryViewSet

medical_history_list = MedicalHistoryViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

medical_history_detail = MedicalHistoryViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path(
        "",
        medical_history_list,
        name="list",
    ),
    path("<int:pk>/", medical_history_detail, name="medical-history-detail"),
]
