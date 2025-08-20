from django.urls import path, include
# from rest_framework import routers

# from . import api
from . import views

# router = routers.DefaultRouter()
# router.register(r'invoice', api.InvoiceViewSet)
# router.register(r'invoiceitem', api.InvoiceItemViewSet)
# router.register(r'payment', api.PaymentViewSet)

urlpatterns = (
    path('purchase/invoice/', 
        views.PurchaseInvoiceListView.as_view(), 
        name='purchase_home'),
)
# urlpatterns = (
#     # urls for Django Rest Framework API
#     path('api/v1/', include(router.urls)),
# )

urlpatterns += (
    # urls for Invoice
    path('invoice/', views.PurchaseInvoiceListView.as_view(), name='purchase_invoice_list'),
    path('invoice/create/', views.PurchaseInvoiceCreateView.as_view(), name='purchase_invoice_create'),
    path('invoice/detail/<int:pk>/', views.PurchaseInvoiceDetailView.as_view(), name='purchase_invoice_detail'),
    path('invoice/update/<int:pk>/', views.PurchaseInvoiceUpdateView.as_view(), name='purchase_invoice_update'),
)

urlpatterns += (
    # urls for InvoiceItem
    path('purchase/invoiceitem/', views.PurchaseInvoiceItemListView.as_view(), name='purchase_invoiceitem_list'),
    path('purchase/invoiceitem/create/', views.PurchaseInvoiceItemCreateView.as_view(), name='purchase_invoiceitem_create'),
    path('purchase/invoiceitem/detail/<int:pk>/', views.PurchaseInvoiceItemDetailView.as_view(), name='purchase_invoiceitem_detail'),
    path('purchase/invoiceitem/update/<int:pk>/', views.PurchaseInvoiceItemUpdateView.as_view(), name='purchase_invoiceitem_update'),
)

urlpatterns += (
    # urls for Payment
    path('purchase/payment/', views.PaymentListView.as_view(), name='purchase_payment_list'),
    path('purchase/payment/create/', views.PaymentCreateView.as_view(), name='purchase_payment_create'),
    path('purchase/payment/detail/<int:pk>/', views.PaymentDetailView.as_view(), name='purchase_payment_detail'),
    path('purchase/payment/update/<int:pk>/', views.PaymentUpdateView.as_view(), name='purchase_payment_update'),
)

