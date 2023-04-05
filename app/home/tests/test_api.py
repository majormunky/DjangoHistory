import datetime
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from home.models import Publication, Edition
from home.api.serializers import PublicationSerializer


PUB_URL = reverse("home:publication-list")
EDITION_URL = reverse("home:edition-list")
PAGE_URL = reverse("home:page-list")


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

    def test_retrieve_publications(self):
        """Test auth is required to call API"""
        create_publication(code="abc123", short_name="abc123", name="abc")
        create_publication(code="dfe456", short_name="dfe123", name="dfe")

        publications = Publication.objects.all()
        pub_serializer = PublicationSerializer(publications, many=True)

        res = self.client.get(PUB_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, pub_serializer.data)


class PublicEditionAPITests(TestCase):
    """Test for unauthenticated API Edition requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(EDITION_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PublicPageAPITests(TestCase):
    """Test for unauthenticated API Page requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(PAGE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
