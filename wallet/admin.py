from django.contrib import admin
from . import models



@admin.register(models.Wallet)
class userAdmin(admin.ModelAdmin):
    list_display = ["user","total_balance"]



@admin.register(models.Deposit)
class Deposit(admin.ModelAdmin):
    list_display = ["user", "amount","status"]
    list_filter = ["user"]
    search_fields = ["amount"]


@admin.register(models.Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["user", "amount"]
    list_filter = ["user"]
    search_fields = ["amount"]
