from rest_framework import serializers
from catalogs.models import Speciality
from django_countries.fields import Country



class SpecialitySerializer(serializers.ModelSerializer):
    """_Summary_
    Serializer for the specialities catalog.

    """

    class Meta:
        model = Speciality
        fields = "__all__"

class CountrySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=2)
    name = serializers.CharField(max_length=255)
    flat = serializers.SerializerMethodField()

    def get_flat(self, obj):
        country = Country(code=obj["code"])
        return country.flat


