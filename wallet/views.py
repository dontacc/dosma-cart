from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers




class WalletView(APIView):
    def get(self, request):
        WalletList = models.Wallet.objects.all()
        serializer = serializers.WalletSerializer(WalletList, many=True)
        return Response(serializer.data)

    def post(self, request):
        if len(models.Wallet.objects.all()) == 1:
            return Response("شما یک کیف پول از قبل دارید", status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.WalletSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            # total_balance = sum([item.amount for item in models.Deposit.objects.all()] \
            #                     + [item.amount for item in models.Withdraw.objects.all()])
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

    # def total(self,request):
    #     deposits = sum([item.amount for item in Deposit.objects.all()])
    #     withdraws = sum([item.amount for item in Withdraw.objects.all()])
    #     self.total_balance = (deposits - withdraws)
    #     super().save(*args,**kwargs)
    #     return self.total_balance


class DepositView(APIView):
    def get(self, request):
        depositList = models.Deposit.objects.all()
        serializer = serializers.DepositSerializer(depositList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.DepositSerializer(data=request.data)
        if serializer.is_valid():
            wallet = serializer.validated_data.get("wallet")
            amount = serializer.validated_data.get("amount")
            serializer.save()
            return Response(status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WithdrawView(APIView):
    def get(self, request):
        withdrawList = models.Withdraw.objects.all()
        serializer = serializers.WithdrawSerializer(withdrawList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.WithdrawSerializer(data=request.data)
        if serializer.is_valid():
            wallet = serializer.validated_data.get("wallet")
            amount = serializer.validated_data.get("amount")
            if amount >= models.Wallet.total(self):
                return Response("موجودی کافی نیست!", status=status.HTTP_400_BAD_REQUEST)
            elif models.Wallet.total(self) - 10 < amount:
                return Response("10 هزار تومان باید در حساب بماند", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
