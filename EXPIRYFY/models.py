from django.db import models

from django.db import models

class Product(models.Model):
    rack_no = models.CharField(max_length=50, unique=True)
    batch_no = models.CharField(max_length=50)
    product_name = models.CharField(max_length=200)
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return f"{self.product_name} - {self.rack_no}"

