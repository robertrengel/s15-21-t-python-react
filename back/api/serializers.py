from rest_framework import serializers

class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    iso3 = serializers.CharField(max_length=3)
    isonum = serializers.CharField(max_length=3)
    title = serializers.CharField(max_length=100)

class RoleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
