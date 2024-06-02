from rest_framework import serializers
from catalogs.models import Speciality
from abstracts.serializers import AbstractSerializer


class SpecialitySerializer(serializers.ModelSerializer):
    """_Summary_
    Serializer for the specialities catalog.

    """

    class Meta:
        model = Speciality
        fields = "__all__"
