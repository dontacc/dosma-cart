from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_balance = models.FloatField(default=0)


    def total(self):
        withdraw = sum([item.amount for item in Withdraw.objects.all()])
        deposit = sum([item.amount for item in Deposit.objects.all()])
        return deposit - withdraw



    def __str__(self):
        return self.user.username


class Deposit(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Deposit"




class Withdraw(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Withdraw"


