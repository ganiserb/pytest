from django.db import models


class Devotional(models.Model):
    title = models.CharField()
    date = models.DateField()
    body = models.TextField()