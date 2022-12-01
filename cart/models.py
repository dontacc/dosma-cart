# Create your models here.
from api.models import product
from django.contrib.auth.models import User
from django.db import models



# sabade kharid
class Cart(models.Model):

    CASH = "نقدی"
    ONLINE = "آنلاین"
    WALLET = "کیف پول"

    PAYMENT_KINDS = [
        (CASH, "cash"),
        (ONLINE, 'online'),
        (WALLET, 'wallet'),
    ]

    # class PaymentKind(models.IntegerChoices):
    #     CASH = 1 , "نقدی"
    #     ONLINE = 2 , "آنلاین"
    #     WALLET = 3 , "کیف پول "

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(null=False,default=False)
    payment_date = models.DateTimeField  # karbari ke sabade kharid barash baz mishe hamon lahze ke
    product = models.ForeignKey(product, on_delete=models.CASCADE,null=True)
    payment = models.CharField(max_length=10,choices=PAYMENT_KINDS, help_text="choose one of the method for payment!" \
                               ,default=ONLINE)
    # Cart.PaymentKind.CASH

    def __str__(self):
        return self.user.username

# class cartItem(models.Model):
#     order = models.OneToOneField(cart, on_delete=models.CASCADE, null=True, related_name="items", blank=True)
#     # in items other ro mitonim dar field haye on yeki class dar serializer estefade konim
#     product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True, related_name="cartitems")
#
#     def __str__(self):
#         return self.product.title
