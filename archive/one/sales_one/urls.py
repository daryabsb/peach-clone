from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'invoice', api.InvoiceViewSet)
router.register(r'invoiceitem', api.InvoiceItemViewSet)
router.register(r'Receive', api.ReceiveViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Invoice
    path('sales/invoice/', views.InvoiceListView.as_view(), name='sales_invoice_list'),
    path('sales/invoice/create/', views.InvoiceCreateView.as_view(), name='sales_invoice_create'),
    path('sales/invoice/detail/<slug:slug>/', views.InvoiceDetailView.as_view(), name='sales_invoice_detail'),
    path('sales/invoice/update/<slug:slug>/', views.InvoiceUpdateView.as_view(), name='sales_invoice_update'),
)

urlpatterns += (
    # urls for InvoiceItem
    path('sales/invoiceitem/', views.InvoiceItemListView.as_view(), name='sales_invoiceitem_list'),
    path('sales/invoiceitem/create/', views.InvoiceItemCreateView.as_view(), name='sales_invoiceitem_create'),
    path('sales/invoiceitem/detail/<int:pk>/', views.InvoiceItemDetailView.as_view(), name='sales_invoiceitem_detail'),
    path('sales/invoiceitem/update/<int:pk>/', views.InvoiceItemUpdateView.as_view(), name='sales_invoiceitem_update'),
)

urlpatterns += (
    # urls for Receive
    path('sales/Receive/', views.ReceiveListView.as_view(), name='sales_receive_list'),
    path('sales/Receive/create/', views.ReceiveCreateView.as_view(), name='sales_Receive_create'),
    path('sales/Receive/detail/<slug:slug>/', views.ReceiveDetailView.as_view(), name='sales_Receive_detail'),
    path('sales/Receive/update/<slug:slug>/', views.ReceiveUpdateView.as_view(), name='sales_Receive_update'),
)

