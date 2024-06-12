from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Doc360User
from api.serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.schemas import ManualSchema
import coreapi
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ApiTokenObtainPairSerializer
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action


class Doc360TokenObtainPairView(TokenObtainPairView):
    serializer_class = ApiTokenObtainPairSerializer


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Doc360User.objects.all()
        serializer = UserCreateSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
def user_list(request):
    queryset = Doc360User.objects.all()
    serializer = UserCreateSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def user_detail(request, id):
    profile = get_object_or_404(Doc360User, pk=id)
    serializer = UserCreateSerializer(profile)
    return Response(serializer.data)


class CustomUserViewSet(UserViewSet):

    @action(method=["post"], detail=False)
    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "EUREKA"}, status=status.HTTP_201_CREATED)
