from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ApiUser, MedicData
from .serializers import UserSerializer, ProfileSerializer

#def hola(request):
#    queryset = ApiUser.objects.all()
#    return render(request, 'test.html', {'users': queryset})

@api_view()
def user_list(request):
    queryset = ApiUser.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def user_detail(request, id):
    profile = get_object_or_404(ApiUser, pk=id)
    serializer = UserSerializer(profile)
    return Response(serializer.data)

'''
@api_view()
def role_list(request):
    queryset = Role.objects.all()
    serializer = RoleSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def role_detail(request, id):
    role = get_object_or_404(Role, pk=id)
    serializer = RoleSerializer(role)
    return Response(serializer.data)
'''