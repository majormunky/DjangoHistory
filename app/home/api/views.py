from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from home.models import Publication
from home.api import serializers


class PublicationViewSet(viewsets.ModelViewSet):
    """Viewset for the publication API"""

    serializer_class = serializers.PublicationSerializer
    queryset = Publication.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
