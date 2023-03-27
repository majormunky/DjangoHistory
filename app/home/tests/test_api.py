import datetime
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from home.models import Publication, Edition
from home.api.serializers import PublicationSerializer


PUB_URL = reverse("home:publication-list")


def create_publication(**params):
    defaults = {
        "name": "Test Publication",
        "short_name": "TestPublication",
        "code": "abc123",
    }
    defaults.update(params)
    new_publication = Publication.objects.create(**defaults)
    return new_publication


def create_edition(pub, **params):
    defaults = {"publish_date": datetime.datetime.today().date(), "page_count": 10}
    defaults.update(params)
    new_edition = Edition.objects.create(publication=pub, **defaults)
    return new_edition


class PublicPublicationAPITests(TestCase):
    """Test for unauthenticated API Publication Requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(PUB_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePublicationAPITests(TestCase):
    """Test for authenticated API Publication Requests"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@example.com", "testpassword1234"
        )
        self.client.force_authenticate(self.user)

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(PUB_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)