import datetime
from django.test import TestCase
from home import models


def build_sample_publication():
    pub_name = "New Publication"
    short_name = "NewPublication"
    code = "123456"
    new_publication = models.Publication(
        name=pub_name, short_name=short_name, code=code
    )
    new_publication.save()
    return new_publication


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


class TestEditions(TestCase):
    def test_create_edition_works(self):
        test_pub = build_sample_publication()
        pub_date = datetime.date(2022, 1, 2)
        page_count = 6
        new_edition = models.Edition(
            publication=test_pub, publish_date=pub_date, page_count=page_count
        )
        new_edition.save()

        self.assertEqual(new_edition.publication, test_pub)
        self.assertEqual(new_edition.publish_date, pub_date)
        self.assertEqual(new_edition.page_count, page_count)
