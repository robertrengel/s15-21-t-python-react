from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models import Doc360User
from django_countries.serializer_fields import CountryField


class ApiTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["user_id"] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({"user_id": self.user.id, "email": self.user.email})
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    user_country = CountryField()

    class Meta:
        model = Doc360User
        fields = fields = [
            "id",
            "email",
            "password",
            "name",
            "first_name",
            "last_name",
            "user_country",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Doc360User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data["name"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            user_country=validated_data["user_country"],
        )
        return user
