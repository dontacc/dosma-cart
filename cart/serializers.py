from api.models import product
from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


# nested serializers
class sampleProductSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(view_name='detail-page' ,read_only=True,lookup_url_kwarg="slug")
    class Meta:
        model = product
        fields = ["id", "title", "price"]


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


# class cartItemSerializer(serializers.ModelSerializer):
#     order = serializers.StringRelatedField()
#     product = sampleProductSerializer(many=False)
#
#     class Meta:
#         model = models.cartItem
#         fields = ["id", "order", "product"]


class CartSerializer(serializers.ModelSerializer):
    # user = serializers.SlugField()
    # product = sampleProductSerializer()
    class Meta:
        model = models.Cart
        fields = ["id","user", "is_paid","product","payment"]










