from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Speciality
from .serializers import SpecialitySerializer

@api_view()
def speciality_list(request):
    queryset = Speciality.objects.all()
    serializer = SpecialitySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def speciality_detail(request, id):
    speciality = get_object_or_404(Speciality, pk=id)
    serializer = SpecialitySerializer(speciality)
    return Response(serializer.data)
