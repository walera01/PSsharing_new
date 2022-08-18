from django.db import models

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
    order_date = models.DateTimeField()
    order_date_end = models.DateTimeField()
    prod = models.ForeignKey("ProductModel", on_delete=models.CASCADE)

