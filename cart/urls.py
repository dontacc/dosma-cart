from django.urls import path
from .view import Cart,DeleteItem ,callback,gateway
from django.views.decorators.cache import cache_page





urlpatterns = [
    path("", Cart.CartView.as_view(), name="cart-status"), # cart
    path("<int:pk>" , DeleteItem.DetailItemView.as_view() , name="detail-page"), # delete item
    path("purchased/", Cart.PurchasedView.as_view(), name="purchased-page"), # purchased products
    path("go-to-gateway/" , gateway.Payment.as_view() , name="gateway-page"), # gateway
    path("callback-gateway/" , callback.CallBackView.as_view() , name="callback-page"), # callback-
]