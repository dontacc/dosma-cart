# GateWay
import logging

from azbankgateways import bankfactories
from azbankgateways import models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers
from .permissions import IsStaffOrReadOnly


class WalletView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        wallet = get_object_or_404(models.Wallet, user_id=request.user.id)
        serializer = serializers.WalletSerializer(wallet, read_only=True)
        return Response(serializer.data)

    def post(self, request):
        current_wallet = models.Wallet.objects.get_or_create(user_id=request.user.id)
        serailizer = serializers.WalletSerializer(current_wallet, many=False)
        return Response(status=status.HTTP_201_CREATED)


class DepositView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Deposit History
    def get(self, request):
        try:
            depoistList = models.Deposit.objects.filter(user_id=request.user.id, status=True)
        except:
            return Response("تراکنشی موجود نیست", status=status.HTTP_200_OK)
        serializer = serializers.DepositSerializer(depoistList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.DepositSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            Amount = serializer.validated_data.get("amount")
            serializer.save()

            amount = Amount
            # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
            user_mobile_number = '+989112221234'  # اختیاری
            factory = bankfactories.BankFactory()
            try:
                # az create zamani estefade mikonim ke mikhaym be on banke maghsad mostaghim vasl shim va banke
                # dg nadarim, autocreate ag bezanim mire kole gateway haro miagarde toshon ag  banki faild shod
                bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
                bank.set_request(request)
                bank.set_amount(amount)
                # bank.set_client_callback_url(reverse('callback-gateway'))
                bank.set_client_callback_url('/wallet/callback-gateway/')
                bank.set_mobile_number(user_mobile_number)  # اختیاری
                bank_record = bank.ready()
                return bank.redirect_gateway()

            except AZBankGatewaysException as e:
                logging.critical(e)
                # TODO: redirect to failed page.
                raise e
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CallBackView(APIView):
    def get(self, request):
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            logging.debug("این لینک معتبر نیست.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)

        except bank_models.Bank.DoesNotExist:
            logging.debug("این لینک معتبر نیست.")
            return Response(status=status.HTTP_404_NOT_FOUND)

            # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
        if bank_record.is_success:
            # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
            # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.

            obj = models.Deposit.objects.filter(user_id=request.user.id, status=0).last()
            obj.status = 1
            obj.save()  # .save faghat be single obj javab mide yani vaghti .get bashe na .filter

            balance = models.Wallet.objects.get(user_id=request.user.id)
            last_deposit = models.Deposit.objects.filter(user_id=request.user.id).last()
            balance.total_balance = balance.total_balance + last_deposit.amount
            balance.save()
            return Response("پرداخت با موفقیت انجام شد.", status=status.HTTP_201_CREATED)

        # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.

        return Response(
            "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")


class WithdrawView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        withdrawList = models.Withdraw.objects.all()
        serializer = serializers.WithdrawSerializer(withdrawList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.WithdrawSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if amount >= models.Wallet.total(self):
                return Response("موجودی کافی نیست!", status=status.HTTP_400_BAD_REQUEST)
            elif models.Wallet.total(self) - 100000 < amount:
                return Response("10 هزار تومان باید در حساب بماند", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
