from cart import models
from cart import serializers
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        productList = models.Cart.objects.filter(user_id=request.user.id, is_paid=False)
        serializer = serializers.CartSerializer(productList, many=True, context={"request": request})
        return Response(serializer.data)

    # add order
    def post(self, request):
        serializer = serializers.CartSerializer(data=request.data)
        if len(models.Cart.objects.filter(payment_status="NOT_PAID")) >= 3:
            return Response({"detail": "بیشتر از 3 سفارش نمیتونین ثبت کنید"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)

    # @action(detail=False,methods=["put"])
    def put(self, request):
        obj = models.Cart.objects.get(user_id=request.user.id)
        serializer = serializers.CartSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=False, methods=["delete"])
    def delete(self, request):
        models.Cart.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# purchased products
class PurchasedView(APIView):
    def get(self, request):
        items = models.Cart.objects.filter(is_paid=1, user_id=request.user.id)
        serializer = serializers.CartSerializer(items, many=True)
        return Response(serializer.data)
