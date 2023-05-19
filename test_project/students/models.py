from django.db import models
from django.urls import reverse


class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Date = models.DateField()
    Email = models.EmailField(max_length=50)
    Money = models.FloatField()
    Group = models.IntegerField()
    on_delete = models.CASCADE

    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):
        return reverse('students_detail', args=[str(self.id)])
