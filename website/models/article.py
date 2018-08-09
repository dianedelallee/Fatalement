from django.db import models
from django.utils import timezone


class Article(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(default=timezone.now)
    tags = models.CharField(max_length=255)
