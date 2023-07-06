from django.db import models


class Person(models.Model):
    name = models.TextField(max_length=50)
    salary = models.FloatField()
    post = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.name
