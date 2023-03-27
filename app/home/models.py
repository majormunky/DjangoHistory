from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=512, unique=True)
    short_name = models.CharField(max_length=512, unique=True)
    code = models.CharField(max_length=64, unique=True)
