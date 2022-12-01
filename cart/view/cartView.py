from cart import models
from cart import serializers
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action


# class CartView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request):
#         listSituation = models.cart.objects.get_or_create(is_paid=False, user_id=request.user.id)
#         serializer = serializers.cartSerializer(listSituation, many=False)
#
#
#         return Response(serializer.data)
#
    # def post(self, request):
    #     serializer = serializers.cartSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.validated_data.get("user")
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        productList = models.Cart.objects.filter(user_id=request.user.id,is_paid=False)
        serializer = serializers.CartSerializer(productList , many=True,context={"request":request})
        return Response(serializer.data)


    # add order
    def post(self,request):
        serializer = serializers.CartSerializer(data=request.data)
        if len(models.Cart.objects.filter(is_paid=False)) >=1:
            return Response({"detail":"یک سبد خرید باز هنوز دارید"},status=status.HTTP_403_FORBIDDEN)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors)

    @action(detail=False , methods=["delete"])
    def delete(self,request):
        models.Cart.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# purchased products
class PurchasedView(APIView):
    def get(self,request):
        items = models.Cart.objects.filter(is_paid=True,user_id=request.user.id)
        serializer = serializers.CartSerializer(items , many=True)
        return Response(serializer.data)






