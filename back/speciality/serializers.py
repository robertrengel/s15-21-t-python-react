from rest_framework import serializers

class SpecialitySerializer(serializers.Serializer):

    country_code = serializers.CharField(max_length=255, read_only=True)