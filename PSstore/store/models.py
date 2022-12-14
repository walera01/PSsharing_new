from django.db import models
from django.urls import reverse


class ProductModel(models.Model):
    name = models.CharField(name='name',max_length=100)
    description = models.CharField(max_length=1000)
    prise_day = models.FloatField()
    prise_dayafter = models.FloatField()
    prise_week = models.FloatField()
    prise_monthe = models.FloatField()
    img = models.ImageField(verbose_name="Изображение")

class OrderModel(models.Model):
    name = models.CharField(name='name', max_length=100)
    number = models.CharField(max_length=13)
    order_date = models.CharField(max_length=20)
    order_date_end = models.CharField(max_length=20, null=True)
    prod = models.ForeignKey("ProductModel", null=True, on_delete=models.CASCADE)

class GamesModel(models.Model):
    name = models.CharField(name='name', max_length=100)
    description = models.CharField(max_length=1000)
    img = models.ImageField(verbose_name="Изображение")

    def get_absolute_url(self):
        return reverse('main')