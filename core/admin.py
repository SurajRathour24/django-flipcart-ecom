from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']


@admin.register(Cart)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']



@admin.register(OrderPlaced)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'odered_date', 'status']

