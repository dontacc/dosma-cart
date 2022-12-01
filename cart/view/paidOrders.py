from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cart import models
from cart import serializers


#  showing the successfull orders
class PaidOrderView(APIView):
    def get(self,request):
        orderList = models.Cart.objects.filter(is_paid=True)
        return Response(status=status.HTTP_200_OK)