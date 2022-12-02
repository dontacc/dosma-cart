from rest_framework import serializers

from . import models


class WalletSerializer(serializers.ModelSerializer):
    # wallet_user = serializers.SerializerMethodField(method_name="user_list")

    class Meta:
        model = models.Wallet
        fields = ['id','user','total_balance']


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = ["id", "user", "amount", "created","status"]


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Withdraw
        fields = ["id", "user", "amount", "created","status"]
