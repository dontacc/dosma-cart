from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_balance = models.FloatField()

    @property
    def total_balance(self):
        deposits = sum([item.amount for item in Deposit.objects.all()])
        withdraws = sum([item.amount for item in Withdraw.objects.all()])
        self.current_balance = deposits - withdraws
        return self.current_balance




class Deposit(models.Model):
    user = models.OneToOneField(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Deposit"

    def __str__(self):
        return self.user.username




class Withdraw(models.Model):
    user = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Withdraw"

    def __str__(self):
        return self.user.username
