from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from catalogs.models import Speciality
from .serializers import SpecialitySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.permissions import ListAndRetrievePermission


class SpecialityViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [ListAndRetrievePermission]
    """_summary_
    A simple ViewSet for listing or retrieving specialities
    """

    def list(self, request):
        query_set = Speciality.objects.all().order_by("speciality_name")
        serializer = SpecialitySerializer(query_set, many=True)
        return Response(serializer.data)
