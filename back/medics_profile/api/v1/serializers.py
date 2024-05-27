from rest_framework import serializers
from medics_profile.models import MedicProfile


class MedicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicProfile
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
