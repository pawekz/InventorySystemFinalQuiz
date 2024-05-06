from django import forms
from .models import Product, Supplier


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_code', 'product_description', 'product_brand', 'product_price', 'supplier']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'contact_person', 'email', 'phone_number', 'address', 'company_website']
