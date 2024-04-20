from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serialiser class for employee objects

    This serializer serializes/deserializes employee object to/from JSON format

    """

    class Meta:
        model = Employee
        fields = "__all__"
