from django.urls import path
from .views import (
    PurchaseList,
    SaleList,
    PaymentList,
    ReceiveList
)

app_name = "transactions"
urlpatterns = [
    path("purchases", PurchaseList.as_view(), name="purchase-list"),
    path("sales", SaleList.as_view(), name="sale-list"),
    path("payments", PaymentList.as_view(), name="payment-list"),
    path("receives", ReceiveList.as_view(), name="receive-list"),
]
