from django.db import models

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def product_count(self):
        return self.products.count()

    product_count.short_description = "Number of Products"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL, related_name='products', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
