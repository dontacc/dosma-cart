from cart import models
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DetailItemView(APIView):
    # def get(self, request, pk):
    #     product = get_object_or_404(models.cartItem, pk=pk)
    #     serializer = serializers.cartItem(product, context={"request": request},many=False)
    #     return Response(serializer.data)

    def delete(self, request, pk):
        detail = get_object_or_404(models.Cart , pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
