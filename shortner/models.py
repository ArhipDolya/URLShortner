from django.db import models


class URL(models.Model):
    url = models.CharField(max_length=500)
    unique_id = models.CharField(max_length=20)
