from django.contrib import admin
from . import models


@admin.register(models.Wallet)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["user","current_balance"]
    list_filter = ["user"]
    search_fields = ["user"]


@admin.register(models.Deposit)
class Deposit(admin.ModelAdmin):
    list_display = ["user", "amount"]
    list_filter = ["user"]
    search_fields = ["amount"]


@admin.register(models.Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["user", "amount"]
    list_filter = ["user"]
    search_fields = ["amount"]
