from django.contrib import admin
from django.contrib.admin import ModelAdmin 
from home.models import *


# @admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'img', 'description']
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'img', 'description', 'max_quantity', 'min_quantity', 'date_updated', 'category', 'date_uploaded', 'brand']
admin.site.register(Product, ProductAdmin)

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'subject', 'email', 'message', 'date_created', 'status']
admin.site.register(Contact, ContactAdmin)


class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'title', 'quantity', 'order_no', 'amount', 'paid', 'price','date_created']
admin.site.register(Shopcart, ShopcartAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'user', 'last_name', 'email', 'phone', 'amount', 'paid', 'shop_code','pay_code', 'pay_date']
admin.site.register(Payment, PaymentAdmin)