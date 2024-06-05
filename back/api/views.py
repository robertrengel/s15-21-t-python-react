from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import ApiUser
from api.serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


@permission_classes(
    [
        IsAuthenticated,
    ]
)
@api_view()
def user_list(request):
    queryset = ApiUser.objects.all()
    serializer = UserCreateSerializer(queryset, many=True)
    return Response(serializer.data)


@permission_classes(
    [
        IsAuthenticated,
    ]
)
@api_view()
def user_detail(request, id):
    profile = get_object_or_404(ApiUser, pk=id)
    serializer = UserCreateSerializer(profile)
    return Response(serializer.data)
