from django.db import models
from django.contrib.auth import get_user_model


class Zoo(models.Model):
    title = models.CharField(max_length=100)
    name = models.TextField()
    view = models.TextField()
    live = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.title
