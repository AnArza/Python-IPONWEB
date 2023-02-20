from django.contrib import admin
from .models import *


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    ordering = ['user__username']
    list_display = ('user', 'id')


class StoreCategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'id')


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'store_category', 'id')


class ItemCategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'picture_preview', 'id')


class ItemAdmin(admin.ModelAdmin):
    ordering = ['price', 'name']
    list_display = ('name', 'price', 'quantity', 'info', 'picture_preview', 'store', 'category', 'id')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'display_items', 'total_price', 'buy_time', 'id')


class MyBagAdmin(admin.ModelAdmin):
    list_display = ('customer', 'display_items', 'total_price', 'id')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(MyBag, MyBagAdmin)
