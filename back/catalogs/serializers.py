from rest_framework import serializers
from catalogs.models import Speciality
from django_countries.fields import Country


class SpecialitySerializer(serializers.ModelSerializer):
    """_Summary_
    Serializer for the specialities catalog.

    """

    class Meta:
        model = Speciality
        fields = [
            "id",
            "speciality_name",
            "speciality_img_url",
            "speciality_description",
        ]


class CountrySerializer(serializers.Serializer):
    """_summary_
    Delivers country information as catalog

    Args:
        code (str): to be used as the country code
        name (str): to be used as the country name
    """

    code = serializers.CharField(max_length=2)
    name = serializers.CharField(max_length=100)
    # flag = serializers.SerializerMethodField()

    # def get_flag(self, obj):
    #     country = Country(code=obj["code"])
    #     return country.flag
