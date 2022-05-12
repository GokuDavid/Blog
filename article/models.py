from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Article(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title