from django.db import models


class Table(models.Model):
    name = models.TextField()
    view = models.TextField()
    live = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name



