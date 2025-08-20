from django.urls import path
from .views import (
    PurchaseList, SaleList, PaymentList, ReceiveList, CreatePurchase, CreateSale,
    CreatePayment, CreateReceive, InvoiceList, InvoiceDetail, CreateInvoice, 
    CustomerSaleView, VendorPurchaseView, create_invoice, add_invoice_items,)

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
    path("invoices/<int:pk>/", InvoiceDetail.as_view(), name="invoice-detail"),
    path("invoices/add/<pk>/", add_invoice_items, name="add-items"),
    # path("invoices/<int:pk>/add/", add_invoice_items, name="invoice-item"),
    path("invoices/create/", create_invoice, name="invoice-create"),
]
