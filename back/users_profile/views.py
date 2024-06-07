from api.models import ApiUser
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ApiUser.objects.all()
