from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from . import models


class WalletSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField(method_name="total_balance")
    user = serializers.SerializerMethodField(method_name="user_list")

    class Meta:
        model = models.Wallet
        fields = ["id", "user", "balance"]

    def total_balance(self, item):
        deposit = sum([item.amount for item in models.Deposit.objects.all()])
        withdraw = sum([item.amount for item in models.Withdraw.objects.all()])
        return deposit - withdraw






    def user_list(self, value):
        return {
            "username": value.user.username,
            "first_name": value.user.first_name
        }


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["id", "wallet", "amount", "created"]


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["id", "wallet", "amount", "created"]
