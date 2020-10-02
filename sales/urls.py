from django.urls import path, include
# from rest_framework import routers

# from . import api
from . import views

# router = routers.DefaultRouter()
# router.register(r'invoice', api.InvoiceViewSet)
# router.register(r'invoiceitem', api.InvoiceItemViewSet)
# router.register(r'receipt', api.ReceiptViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    # path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Invoice
    path('invoice/', views.InvoiceListView.as_view(), name='sales_invoice_list'),
    path('invoice/create/', views.InvoiceCreateView.as_view(), name='sales_invoice_create'),
    path('invoice/detail/<int:pk>/', views.InvoiceDetailView.as_view(), name='sales_invoice_detail'),
    path('invoice/update/<int:pk>/', views.InvoiceUpdateView.as_view(), name='sales_invoice_update'),
)

urlpatterns += (
    # urls for InvoiceItem
    path('invoiceitem/', views.InvoiceItemListView.as_view(), name='sales_invoiceitem_list'),
    path('invoiceitem/create/', views.InvoiceItemCreateView.as_view(), name='sales_invoiceitem_create'),
    path('invoiceitem/detail/<int:pk>/', views.InvoiceItemDetailView.as_view(), name='sales_invoiceitem_detail'),
    path('invoiceitem/update/<int:pk>/', views.InvoiceItemUpdateView.as_view(), name='sales_invoiceitem_update'),
)

# urlpatterns += (
#     # urls for Receipt
#     path('sales/receipt/', views.ReceiptListView.as_view(), name='sales_receipt_list'),
#     path('sales/receipt/create/', views.ReceiptCreateView.as_view(), name='sales_receipt_create'),
#     path('sales/receipt/detail/<slug:slug>/', views.ReceiptDetailView.as_view(), name='sales_receipt_detail'),
#     path('sales/receipt/update/<slug:slug>/', views.ReceiptUpdateView.as_view(), name='sales_receipt_update'),
# )

