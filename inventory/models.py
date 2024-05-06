from django.db import models

# Create your models here.

class Supplier (models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.TextField()
    company_website = models.URLField(max_length=100)

    def __str__(self):
        return self.supplier_name



class Product (models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100)
    product_description = models.TextField()
    product_brand = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
