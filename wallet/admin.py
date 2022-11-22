from django.contrib import admin
from . import models



@admin.register(models.Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["user","total_balance"]



@admin.register(models.Deposit)
class Deposit(admin.ModelAdmin):
    list_display = ["wallet", "amount"]
    list_filter = ["wallet"]
    search_fields = ["amount"]


@admin.register(models.Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["wallet", "amount"]
    list_filter = ["wallet"]
    search_fields = ["amount"]
