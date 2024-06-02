from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ApiUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



@api_view()
@permission_classes([IsAuthenticated])
def user_list(request):
    queryset = ApiUser.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
def user_detail(request, id):
    profile = get_object_or_404(ApiUser, pk=id)
    serializer = UserSerializer(profile)
    return Response(serializer.data)
