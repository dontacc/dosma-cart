from cart import models
from cart import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
# Cache
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie,vary_on_headers
# Gateway
import logging
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from rest_framework import permissions


# @method_decorator([vary_on_cookie,cache_page(20)] , name="dispatch")
class CartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # current_orders = models.cartItem.objects.filter(order_id).all()
        product = models.cartItem.objects.all()
        serializer = serializers.cartItemSerializer(product, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.cartItemSerializer(data=request.data)  # request.data hamon dataye vared shodas
        if serializer.is_valid():
            order = serializer.validated_data.get("order")
            product = serializer.validated_data.get("product")
            serializer.save()
            return Response(f"{product.title} به سبد خرید اضافه شد",status=status.HTTP_201_CREATED)




    # baraye inke listi ro hazf konim view be sorate generic nadarim bayad dasti benevisim joda
    @action(detail=False, methods=["delete"])
    def delete(self, request):
        models.cartItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
