from rest_framework import serializers

class SpecialitySerializer(serializers.Serializer):

    id = serializers.IntegerField()
    speciality = serializers.CharField(max_length=255, read_only=True)
    image_url = serializers.CharField(max_length=100, read_only=True)