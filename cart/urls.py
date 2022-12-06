from django.urls import path
from .view import cartView  , detailitemView , gateway,callback
from django.views.decorators.cache import cache_page





urlpatterns = [
    path("" , cartView.CartView.as_view() , name="cart-status"), # cart
    path("<int:pk>" , detailitemView.DetailItemView.as_view() , name="detail-page"), # delete all items
    path("purchased/" , cartView.PurchasedView.as_view() , name="purchased-page"), # purchased products
    path("go-to-gateway/" , gateway.Payment.as_view() , name="gateway-page"), # gateway
    path("callback-gateway/" , callback.CallBackView.as_view() , name="callback-page"), # callback-
]