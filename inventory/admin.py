from django.contrib import admin

from inventory.models import Supplier, Product

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Product)
