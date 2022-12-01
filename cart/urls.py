from django.urls import path
from .view import cartView  , detailitemView , gateway,callback , paidOrders
from django.views.decorators.cache import cache_page





urlpatterns = [
    # path("" , cartitemView.CartItemView.as_view() ,name="cart-list"), # order
    path("" , cartView.CartView.as_view() , name="cart-status"), # cart
    path("<int:pk>" , detailitemView.DetailItemView.as_view() , name="detail-page"), #
    path("purchased/" , cartView.PurchasedView.as_view() , name="purchased-page"),
    path("go-to-gateway/" , gateway.PaymentGateway.as_view() , name="gateway-page"), # gateway
    path("callback-gateway/" , callback.CallBackView.as_view() , name="callback-page"), # callback-
    path("done-orders/" , paidOrders.PaidOrderView.as_view() , name="done-orders"),
]