from api.models import ApiUser
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()

    # Create your views here.
    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAuthenticated,
            ]  # Or any other permissions you need
        return super().get_permissions()
