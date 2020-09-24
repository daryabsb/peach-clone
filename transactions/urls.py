from django.urls import path
from .views import (
    PurchaseList,
    SaleList,
    PaymentList,
    ReceiveList,
    CreatePurchase,
    CreateSale,
    CreatePayment,
    CreateReceive,
    InvoiceList,
    CreateInvoice,
    CustomerSaleView,
    VendorPurchaseView
)

app_name = "transactions"
urlpatterns = [
    path("purchases", PurchaseList.as_view(), name="purchase-list"),
    path("sales", SaleList.as_view(), name="sale-list"),
    path("payments", PaymentList.as_view(), name="payment-list"),
    path("receives", ReceiveList.as_view(), name="receive-list"),
    path("revenues", CustomerSaleView.as_view(), name="revenues-list"),
    path("inventories", VendorPurchaseView.as_view(), name="inventories-list"),
    path("purchases/add/", CreatePurchase.as_view(), name="purchase-add"),
    path("sales/add/", CreateSale.as_view(), name="sale-add"),
    path("payments/add/", CreatePayment.as_view(), name="payment-add"),
    path("receives/add/", CreateReceive.as_view(), name="receive-add"),
    path("invoices/", InvoiceList.as_view(), name="invoice-list"),
    path("invoices/add/", CreateInvoice.as_view(), name="invoice-add"),
]
