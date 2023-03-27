from rest_framework import serializers
from home.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ["id", "name", "short_name", "code"]
        read_only_fields = ["id"]
