from django.test import TestCase
from home import models


class TestPublications(TestCase):
    def test_create_publication_works(self):
        pub_name = "New Publication"
        short_name = "NewPublication"
        code = "123456"
        new_publication = models.Publication(
            name=pub_name, short_name=short_name, code=code
        )
        new_publication.save()

        self.assertEqual(new_publication.name, pub_name)
        self.assertEqual(new_publication.short_name, short_name)
        self.assertEqual(new_publication.code, code)
