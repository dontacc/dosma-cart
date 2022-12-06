# Create your models here.
from api.models import product
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


PAYMENT_KIND = (
    ("NOT_PAID", "پرداخت نشده"),
    ("ONLINE", "آنلاین"),
    ("CASH", "نقدی")
)

IS_PAID = (
    (0,"پرداخت نشده"),
    (1,"پرداخت شده ")
)


# sabade kharid
class Cart(models.Model):
    # CASH = "نقدی"
    # ONLINE = "آنلاین"
    # WALLET = "کیف پول"
    #
    # PAYMENT_KINDS = [
    #     (CASH, "cash"),
    #     (ONLINE, 'online'),
    #     (WALLET, 'wallet'),
    # ]

    # class PaymentKind(models.IntegerChoices):
    #     CASH = 1, "نقدی"
    #     ONLINE = 2, "آنلاین"
    #     WALLET = 3, "کیف پول"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.SmallIntegerField(choices=IS_PAID,null=False, default=0)
    payment_date = models.DateTimeField  # karbari ke sabade kharid barash baz mishe hamon lahze ke
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=32,choices=PAYMENT_KIND,
                                      help_text="choose one of the method for payment!" \
                                      , default="NOT_PAID")
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username
