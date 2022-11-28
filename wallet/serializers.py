from rest_framework import serializers

from . import models


class WalletSerializer(serializers.ModelSerializer):
    total_balance = serializers.SerializerMethodField(method_name="total")
    user = serializers.SerializerMethodField(method_name="user_list")

    class Meta:
        model = models.Wallet
        fields = ["id", "user","total_balance"]

    def total(self, item):
        deposit = sum([item.amount for item in models.Deposit.objects.all()])
        withdraw = sum([item.amount for item in models.Withdraw.objects.all()])
        return deposit - withdraw

    def user_list(self, value):
        return {
            "id":value.user.id,
            "username": value.user.username,
            "first_name": value.user.first_name
        }


class DepositSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Deposit
        fields = ["id", "user", "amount", "created","status"]


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["id", "user", "amount", "created","status"]
