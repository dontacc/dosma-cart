from django.urls import path
from .view import cartView ,cartitemView , detailitemView , gateway,callback
from django.views.decorators.cache import cache_page





urlpatterns = [
    path("" , cartitemView.CartItemView.as_view() ,name="cart-list"), # order
    path("situation/" , cartView.CartView.as_view() , name="cart-status"), # cart
    path("<int:pk>" , detailitemView.DetailItemView.as_view() , name="detail-page"), #
    path("go-to-gateway/" , gateway.paymentGateaway.as_view() , name="gateway-page"), # gateway
    path("callback-gateway/" , callback.CallBackView.as_view() , name="callback-page") # callback-gateway
]