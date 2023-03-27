import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from home.models import Publication, Edition
from home.api.serializers. import PublicationSerializer


def create_publication(**params):
    defaults = {
        "name": "Test Publication",
        "short_name": "TestPublication",
        "code": "abc123"
    }
    defaults.update(params)
    new_publication = Publication.objects.create(**defaults)
    return new_publication


def create_edition(pub, **params):
    defaults = {
        "publish_date": datetime.datetime.today().date(),
        "page_count": 10
    }
    defaults.update(params)
    new_edition = Edition.objects.create(publication=pub, **defaults)
