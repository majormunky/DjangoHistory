from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from home.models import Publication, Edition
from home.api import serializers


class PublicationViewSet(viewsets.ModelViewSet):
    """Viewset for the publication API"""

    serializer_class = serializers.PublicationSerializer
    queryset = Publication.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class EditionViewSet(viewsets.ModelViewSet):
    """Viewset for the edition API"""

    serializer_class = serializers.EditionSerializer
    queryset = Edition.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
