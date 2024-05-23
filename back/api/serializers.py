from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    uniqueid = serializers.CharField(max_length=50)
    country_code = serializers.CharField(max_length=3)
    role = serializers.CharField(max_length=3)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    id_type = serializers.CharField(max_length=255)
    id_value = serializers.CharField(max_length=255)
    genre = serializers.CharField(max_length=255)
    civil_status = serializers.CharField(max_length=255)
    birth_date = serializers.DateField()
    created_by = serializers.CharField(max_length=50)
    added_date = serializers.DateTimeField()
    modified_date = serializers.DateTimeField()
    


class ProfileSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    email = serializers.EmailField(max_length=100)
    notifications = serializers.BooleanField()
