from django.contrib import admin
from . import models
# Register your models here.




# @admin.register(models.cartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ["product","order"]


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user","is_paid","product"]
