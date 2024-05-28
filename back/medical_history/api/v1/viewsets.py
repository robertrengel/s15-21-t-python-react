from rest_framework import viewsets, filters, status

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from medical_history.models import MedicalHistory

from medical_history.api.v1.serializers import MedicalHistorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["medical_history"])
class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

    def get_queryset(self):
        queryset = MedicalHistory.objects.all()

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            data = {
                "status": "success",
                "data": serializer.data,
                "status_code": status.HTTP_201_CREATED,
            }
            headers = self.get_success_headers(serializer.data)
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError as e:
            data = {
                "status": "error",
                "message": str(e),
                "status_code": status.HTTP_400_BAD_REQUEST,
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)
