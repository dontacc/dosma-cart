"""drf_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from azbankgateways.urls import az_bank_gateways_urls
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("restframework-auth", include('rest_framework.urls')),
    path("api/", include("api.urls")),

    # JWT
    # path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    # path("token/verify" , jwt_views.TokenVerifyView.as_view() , name="token_verify"),

    # Cart
    path("carts/", include("cart.urls")),

    # payment gateways
    path("bankgateways/", az_bank_gateways_urls()),

    # Wallet
    path("wallet/", include("wallet.urls")),
]
