from rest_framework import viewsets, status

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from medical_history.models import MedicalHistory
from rest_framework.authentication import TokenAuthentication
from medical_history.api.v1.serializers import MedicalHistorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.permissions import IsAuthenticatedToViewList


class MedicalHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = MedicalHistorySerializer

    def list(self, request, *wargs, **kwargs):
        """
        Return a list of all the existing items.
        Only active clinical expedient
        """
        queryset = MedicalHistory.objects.all().order_by("title")
        serializer = MedicalHistorySerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        CRUD functionality: Create (create a new clinical expedient)
        **URL:** `POST /medical-history/`
        -
        **Request Body:**
        - `added_by` (int): Positive integer | This field is validated from the side server

        """
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

    def retrive(self, request, *args, **kwargs):

        medical_id = kwargs.get("pk")
        try:
            medical_id_fetched = MedicalHistory.objects.get(id=medical_id)
        except medical_id_fetched.DoesNotExist:
            return Response(
                {"details": "Medical History not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        extra_data = {"extra_info": "This is additional data"}
        serializer = self.get_serializer(medical_id_fetched)
        response_data = serializer.data
        response_data.update(extra_data)
        return Response(response_data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a specific medical history by ID.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": "Medical history deleted."}, status=status.HTTP_204_NO_CONTENT
        )
