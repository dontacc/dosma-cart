from cart import models
from cart import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


class CartItemView(APIView):
    def get(self, request):

        listCart = models.cartItem.objects.all()
        serializer = serializers.cartItemSerializer(listCart, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        if len(models.cartItem.objects.all()) == 1:
            return Response("در سبد خرید شما یک سفارش وجود دارد")
        serializer = serializers.cartItemSerializer(data=request.data)  # request.data hamon dataye vared shodas
        if serializer.is_valid():
            order = serializer.validated_data.get("payment")
            product = serializer.validated_data.get("product")
            serializer.save()
            return Response({"message": "product added to the cart!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # baraye inke listi ro hazf konim view be sorate generic nadarim bayad dasti benevisim joda
    @action(detail=False, methods=["delete"])
    def delete(self, request):
        models.cartItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
