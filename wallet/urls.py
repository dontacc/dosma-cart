from django.urls import path

from . import views

urlpatterns = [
    path("", views.WalletView.as_view(), name="wallet-page"), # wallet
    path("deposits/", views.DepositView.as_view(), name="deposit-page"), # deposit
    path("withdraw/", views.WithdrawView.as_view(), name="withdraw-page"), # withdraw
    path("callback-gateway/" , views.CallBackView.as_view() , name="callback-page") # callback
]
