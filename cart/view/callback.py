import logging

from azbankgateways import models as bank_models, default_settings as settings
from cart import models
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wallet.models import Wallet


class CallBackView(APIView):
    def get(self, request):
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            logging.debug("این لینک معتبر نیست.")
            raise Http404
        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)

        except bank_models.Bank.DoesNotExist:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

        if bank_record.is_success:

            # adding to balance
            wallet_balance = Wallet.objects.get(user_id=request.user.id)
            cart = models.Cart.objects.filter(user_id=request.user.id,payment_status="ONLINE",is_paid=0)
            new_balance = sum([item.product.price for item in cart]) - wallet_balance.total_balance
            # jame order ha - balance = meghdari ke be gateway rafte va pardakht karde
            wallet_balance.total_balance = wallet_balance.total_balance + new_balance
            wallet_balance.save()

            # obj = models.Cart.objects.get(user_id=request.user.id, is_paid=0,payment_status="ONLINE")
            # obj.payment_status = 1
            # obj.save()


            return Response("پرداخت با موفقیت انجام شد. کیف پول شما شارژ شد", status=status.HTTP_301_MOVED_PERMANENTLY)

        # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
        return HttpResponse(
            "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")
