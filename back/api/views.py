from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Country, Role, CustomUser
from .serializers import CountrySerializer, RoleSerializer

#def hola(request):
#    return render(request, 'test.html', {'name': 'is here'})

@api_view()
def countries_list(request):
    queryset = Country.objects.all()
    serializer = CountrySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def country_detail(request, id):
    country = get_object_or_404(Country, pk=id)
    serializer = CountrySerializer(country)
    return Response(serializer.data)


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
