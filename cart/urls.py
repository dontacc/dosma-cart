from django.urls import path
from .view import cartView ,cartitemView , detailitemView




urlpatterns = [
    path("" , cartitemView.CartItemView.as_view() , name="cart-list"),
    path("situation/" , cartView.CartView.as_view() , name="cart-status"),
    path("<int:pk>" , detailitemView.DetailItemView.as_view() , name="detail-page")
]