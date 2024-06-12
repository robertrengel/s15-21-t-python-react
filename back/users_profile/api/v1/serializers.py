from rest_framework import serializers
from users_profile.models import UserProfile
from django_countries.serializers import CountryFieldMixin
from api.models import Doc360User
from .validators import validate_unique_id


class UserProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    user_country = serializers.CharField(source="user.user_country", read_only=True)
    user_country_name = serializers.CharField(source="user.user_country.name")
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)

    """
    Serializer for the Item model.
    S E R I A L I Z A T I O N
    """

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "first_name",
            "last_name",
            "genre",
            "civil_status",
            "user_country",
            "user_country_name",
            "is_active",
            "civil_status",
            "birth_date",
            "notifications",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    unique_id = serializers.IntegerField(validators=[validate_unique_id])

    class Meta:
        model = UserProfile
        fields = [
            "unique_id",
            "id_type",
            "id_value",
            "genre",
            "civil_status",
            "birth_date",
            "notifications",
            "status",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
            "is_active",
        ]
