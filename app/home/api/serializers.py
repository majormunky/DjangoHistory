from rest_framework import serializers
from home.models import Publication, Edition


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ["id", "name", "short_name", "code"]
        read_only_fields = ["id"]


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ["id", "publish_date", "page_count"]
        read_only_fields = ["id"]
