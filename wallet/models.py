from django.contrib.auth.models import User
from django.db import models

STATUS_KIND = (
    (0, "not paid"),
    (1, "paid")
)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_balance = models.FloatField(default=0)

    def __str__(self):
        return self.user.username


# har deposit yek user dare, va har user chandin deposit mitone dashte bashe
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)
    status = models.SmallIntegerField(choices=STATUS_KIND , default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Deposit"


class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Withdraw"
