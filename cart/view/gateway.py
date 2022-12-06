import logging

from azbankgateways import bankfactories
from azbankgateways.exceptions import AZBankGatewaysException
from cart.models import Cart
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wallet.models import Wallet
from django.http import HttpResponse


# action by default methode get ro mifreste age methodesho malom nakonim
class Payment(APIView):
    def get(self,request):
        amount = sum([item.product.price for item in Cart.objects.filter(user_id=request.user.id)])
        if amount == 0:
            return Response("سفارشی در سبد خرید شما نیست", status=status.HTTP_200_OK)

        cart = Cart.objects.get(user_id=request.user.id)
        wallet = Wallet.objects.get(user_id=request.user.id)

        if cart.payment_status == "ONLINE":
            if amount <= wallet.total_balance:
                wallet.total_balance = wallet.total_balance - amount
                wallet.save()
                return Response(f"از کیف پول شما کم شد{amount}مبلغ", status=status.HTTP_200_OK)
            else:
                new_amount = amount - wallet.total_balance
                user_mobile_number = '+989112221234'  # اختیاری
                factory = bankfactories.BankFactory()
                try:
                    # az create zamani estefade mikonim ke mikhaym be on banke maghsad mostaghim vasl shim va banke
                    # dg nadarim, autocreate ag bezanim mire kole gateway haro miagarde toshon ag  banki faild shod
                    bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
                    bank.set_request(request)
                    bank.set_amount(new_amount)
                    # bank.set_client_callback_url(reverse('callback-gateway'))
                    bank.set_client_callback_url('/carts/callback-gateway/')
                    bank.set_mobile_number(user_mobile_number)  # اختیاری
                    bank_record = bank.ready()
                    return bank.redirect_gateway()
                except AZBankGatewaysException as e:
                    logging.critical(e)
                    # TODO: redirect to failed page.
                    raise e
        else:
            return Response("error")


