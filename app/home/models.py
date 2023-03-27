from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=512, unique=True)
    short_name = models.CharField(max_length=512, unique=True)
    code = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Edition(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    publish_date = models.DateField()
    page_count = models.IntegerField(default=0)

    def __str__(self):
        return "{pub_name}: {pub_date}".format(
            pub_name=self.publication.name,
            pub_date=self.publish_date.strftime("%m-%d-%Y"),
        )
