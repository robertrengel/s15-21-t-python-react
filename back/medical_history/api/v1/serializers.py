from rest_framework import serializers
from medical_history.models import MedicalHistory
from medical_history.validators import validate_added_by_is_positive_integer


class MedicalHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model.
    S E R I A L I Z A T I O N
    """

    class Meta:
        model = MedicalHistory
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

    def validad_added_by(self, value):
        validate_added_by_is_positive_integer(value)
        return value
