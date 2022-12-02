from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class productSerializers(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(view_name="api:detail-page")
    class Meta:
        model = models.product
        fields = "__all__"




class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



# class cartSerializers(serializers.ModelSerializer):
#     user = serializers.CurrentUserDefault()
#     total_price = serializers.IntegerField(read_only=True)
#     class Meta:
#         model = models.Cart
#         fields = "__all__"