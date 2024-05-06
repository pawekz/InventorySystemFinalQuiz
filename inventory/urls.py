from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # This is the default page
    path('add_product/', views.add_product, name='add_product'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('product_list/', views.product_list, name='product_list'),
    path('supplier_list/', views.supplier_list, name='supplier_list'),
    path('supplier/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),
]