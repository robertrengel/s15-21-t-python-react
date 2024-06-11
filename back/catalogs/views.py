from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from catalogs.models import Speciality
from .serializers import SpecialitySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CountrySerializer
from django_countries import countries


class SpecialityViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    """_summary_
    A simple ViewSet for listing or retrieving specialities
    """

    def list(self, request):
        query_set = Speciality.objects.all().order_by("speciality_name")
        serializer = SpecialitySerializer(query_set, many=True)
        return Response(serializer.data)


class CountriesCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = []
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        country_list = [
            {"code": code, "name": name} for code, name in dict(countries).items()
        ]
        serializer = self.get_serializer(country_list, many=True)
        return Response(serializer.data)
