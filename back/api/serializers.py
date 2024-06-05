from rest_framework import serializers
from api.models import ApiUser
from django_countries.serializer_fields import CountryField



class UserCreateSerializer(serializers.ModelSerializer):
    user_country = CountryField()
    class Meta:
        model = ApiUser
        fields = fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "user_country",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = ApiUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            user_country=validated_data["user_country"],
        )
        return user
