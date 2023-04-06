from rest_framework import serializers
from core.models import CoreUser


class CoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreUser
        fields = ["id", "email", "first_name", "last_name"]
        read_only_fields = ["id"]
