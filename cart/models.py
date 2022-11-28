# Create your models here.
from api.models import product
from django.contrib.auth.models import User
from django.db import models


# sabade kharid
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField  # karbari ke sabade kharid barash baz mishe hamon lahze ke

    # pardakht nemikone baraye hamin null va blank mitone bashe ta ye timi

    def __str__(self):
        return self.user.username


class cartItem(models.Model):
    order = models.OneToOneField(cart, on_delete=models.CASCADE, null=True, related_name="items", blank=True)
    # in items other ro mitonim dar field haye on yeki class dar serializer estefade konim
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True, related_name="cartitems")

    def __str__(self):
        return self.product.title



class ShopList(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    product = models.ForeignKey(cartItem , on_delete=models.CASCADE)

