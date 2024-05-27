from rest_framework import viewsets, filters, status

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from medics_profile.models import MedicProfile

from medics_profile.api.v1.serializers import MedicProfileSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["medics_profile"])
class MedicProfileViewSet(viewsets.ModelViewSet):
    queryset = MedicProfile.objects.all()
    serializer_class = MedicProfileSerializer

    def get_queryset(self):
        queryset = MedicProfile.objects.all()

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
