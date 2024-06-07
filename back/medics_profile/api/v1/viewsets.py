from rest_framework import viewsets, status
from rest_framework.response import Response
from medics_profile.models import MedicProfile
from medics_profile.api.v1.serializers import MedicProfileSerializer
from rest_framework.permissions import IsAuthenticated
from utils.permissions import ListAndRetrievePermission


class MedicProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [ListAndRetrievePermission]
    queryset = MedicProfile.objects.all()
    serializer_class = MedicProfileSerializer

    def get_queryset(self):

        queryset = MedicProfile.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        """
        Return a list of all the existing items.
        Only active clinical expedient
        """
        return super().list(request, *args, **kwargs)

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

    def retrive(self, request, *args, **kwargs):

        medical_id = kwargs.get("pk")
        try:
            medical_id_fetched = MedicProfile.objects.get(id=medical_id)
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