from rest_framework import viewsets, status
from rest_framework.response import Response
from users_profile.api.v1.serializers import (
    UserProfileSerializer,
    UserProfileUpdateSerializer,
)

from rest_framework.permissions import IsAuthenticated
from users_profile.models import UserProfile
from api.models import Doc360User
from rest_framework.exceptions import PermissionDenied


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def list(self, request, *wargs, **kwargs):
        """
        Return a list of all the existing items.
        Only active clinical expedient
        """
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)

        return Response(serializer.data)


class UserProfileUpdateViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["put", "patch"]
    serializer_class = UserProfileUpdateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        if instance.user != request.user:
            raise PermissionDenied("You can only update your own profile")
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.perform_update(serializer)
        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    # def retrive(self, request, *args, **kwargs):

    #     medical_id = kwargs.get("pk")
    #     try:
    #         medical_id_fetched = UserProfile.objects.get(id=medical_id)
    #     except medical_id_fetched.DoesNotExist:
    #         return Response(
    #             {"details": "Medical History not found"},
    #             status=status.HTTP_404_NOT_FOUND,
    #         )
    #     extra_data = {"extra_info": "This is additional data"}
    #     serializer = self.get_serializer(medical_id_fetched)
    #     response_data = serializer.data
    #     response_data.update(extra_data)
    #     return Response(response_data)

    # def destroy(self, request, *args, **kwargs):
    #     """
    #     Delete a specific medical history by ID.
    #     """
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(
    #         {"detail": "Medical history deleted."}, status=status.HTTP_204_NO_CONTENT
    #     )
