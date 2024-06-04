from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import ApiUser
from api.serializers import ApiUserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view()
@permission_classes([IsAuthenticated])
def user_list(request):
    queryset = ApiUser.objects.all()
    serializer = ApiUserCreateSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
def user_detail(request, id):
    profile = get_object_or_404(ApiUser, pk=id)
    serializer = ApiUserCreateSerializer(profile)
    return Response(serializer.data)
