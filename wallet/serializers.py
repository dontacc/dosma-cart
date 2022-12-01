from rest_framework import serializers

from . import models


class WalletSerializer(serializers.ModelSerializer):
    total_balance = serializers.SerializerMethodField(method_name="total")
    # wallet_user = serializers.SerializerMethodField(method_name="user_list")

    class Meta:
        model = models.Wallet
        fields = ['id','user','total_balance']

    def total(self, item):
        deposit = sum([item.amount for item in models.Deposit.objects.all()])
        withdraw = sum([item.amount for item in models.Withdraw.objects.all()])
        return deposit - withdraw

    # def user_list(self, value):
    #     return {
    #         "id":value.wallet_user.id,
    #         "username": value.wallet_user.first_name,
    #         "first_name": value.wallet_user.last_name
    #     }


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["id", "user", "amount", "created","status"]


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["id", "user", "amount", "created","status"]
