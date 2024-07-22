from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return self.name
