from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from . import serializers
from . import models
from rest_framework.generics import ListCreateAPIView




class WalletView(APIView):
    def get(self,request):
        WalletList = models.Wallet.objects.all()
        serializer = serializers.WalletSerializer(WalletList , read_only=True)
        return Response(status=status.HTTP_200_OK)



class DepositView(ListCreateAPIView):
    queryset = models.Deposit.objects.all()
    serializer_class = serializers.DepositSerializer




class WithDrewView(ListCreateAPIView):
    queryset = models.Withdraw.objects.all()
    serializer_class = serializers.WithdrawSerializer



# class DepostiView():
#     def post(self,request):
#         serializer = serializers.DepositSerializer(data=request.data)