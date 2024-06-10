from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models import ApiUser
from django_countries.serializer_fields import CountryField


class ApiTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["user_id"] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({"user_id": self.user.id, "username": self.user.username})
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    user_country = CountryField()

    class Meta:
        model = ApiUser
        fields = fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "user_country",
        ]
        exclude_fields = ["email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = ApiUser.objects.create_user(
            username=validated_data["username"],
            # email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            user_country=validated_data["user_country"],
        )
        return user
