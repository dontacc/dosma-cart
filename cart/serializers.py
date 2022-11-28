from api.models import product
from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


# nested serializers
class sampleProductSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedRelatedField(view_name='detail-page' ,read_only=True,lookup_url_kwarg="slug")
    class Meta:
        model = product
        fields = ["id", "title", "price"]


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


# detaile sabade kharid
class cartItemSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField()
    product = sampleProductSerializer(many=False)

    class Meta:
        model = models.cartItem
        fields = ["id", "order", "product"]


class cartSerializer(serializers.ModelSerializer):
    # inja product haye ziadi gharare neshon dade she
    user = userSerializer()

    class Meta:
        model = models.cart
        fields = ["user", "is_paid", "payment_date"]
