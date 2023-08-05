from django.db import models
from django.urls import reverse


class Devices(models.Model):
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=20)
    date = models.DateField()
    quantity_in_pack = models.IntegerField()
    quantity_thing = models.IntegerField()
    packing_price = models.DecimalField(max_digits=6, decimal_places=2)
    price_for_one = models.DecimalField(max_digits=6, decimal_places=2)
    result = models.IntegerField()

    class Meta:
        verbose_name_plural = 'devices'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('devices_list')


class Search(models.Model):
    name = models.CharField(max_length=100), models.ForeignKey(Devices, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "search"

    def __str__(self):
        return self.name


class Select(models.Model):
    name = models.CharField(max_length=100), models.ForeignKey(Devices, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "select"

    def __str__(self):
        return self.name


