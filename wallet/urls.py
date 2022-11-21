from django.urls import path
from . import views



urlpatterns = [
    path("" , views.WalletView.as_view() , name="wallet-page"),
    path("deposits/" , views.DepositView.as_view() , name="deposit-page"),
    path("withdraw/" , views.WithDrewView.as_view() , name="withdraw-page")
]