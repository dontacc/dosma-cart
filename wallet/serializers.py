from rest_framework import serializers

from . import models


class WalletSerializer(serializers.ModelSerializer):
    current_balance = serializers.SerializerMethodField(method_name="total_balance")

    class Meta:
        model = models.Wallet
        fields = ["user", "amount" , "current_balance"]

    def total_balance(self):
        deposits = sum([item.amount for item in Deposit.objects.all()])
        withdraws = sum([item.amount for item in Withdraw.objects.all()])
        return deposits - withdraws


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["id", "user", "amount"]


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["id", "user", "amount"]



