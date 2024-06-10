from rest_framework import serializers


def validate_unique_id(value):
    try:
        value = int(value)
    except ValueError:
        raise serializers.ValidationError("The unique_id must be an integer.")

    if value <= 0:
        raise serializers.ValidationError(
            "The unique_id must be a positive number greater than zero."
        )
    return value
