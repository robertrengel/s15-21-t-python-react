from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models import Doc360User
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from rest_framework import status
from rest_framework.response import Response


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
         #   "name",
            "first_name",
            "last_name",
            "id_nationality",
            "date_brith",
            #"username",
            "password",
            "user_country",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"help_text": "Valid gmail address"},
            "password": {
                "help_text": "min lenght 8 caracters:<br> \
                        1.- Uppercase letter.<br> \
                        2.- Lowercase letter.<br> \
                        3.- Digit number.<br> \
                        4.- Special character: #/%&"
            },
         #   "name": {"help_text": "Full name"},
            "first_name": {"help_text": "Only alfabetic characters"},
            "last_name": {"help_text": "Only alfabetic characters"},
            "user_country": {"help_text": "Country Name"},
        }

    def create(self, validated_data):
        user = Doc360User.objects.create_user(
            email=validated_data["email"],
         #   name=validated_data["name"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            id_nationality=validated_data["id_nationality"],
            date_brith=validated_data["date_brith"],
            #username=validated_data["username"],
            password=validated_data["password"],
            user_country=validated_data["user_country"],
            
        )

        return user



class CustomUserCreateSerializer(UserCreateSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        response_data = {"detail": "User created successfully"}
        return Response(response_data, status=status.HTTP_201_CREATED)
