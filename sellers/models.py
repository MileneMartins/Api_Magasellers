from django.db import models


class Seller(models.Model):
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.description 

PRODUCT_STATUS = [
    ("A", "Active"),
    ("I", "Inative")
]
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    sku = models.CharField(max_length=100)
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=1, choices=PRODUCT_STATUS, default="A")

    def __str__(self):
        return self.title
