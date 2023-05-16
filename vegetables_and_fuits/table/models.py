from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=100)
    type = models.TextField()
    colour = models.TextField()
    calories = models.TextField()
    short_description = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
