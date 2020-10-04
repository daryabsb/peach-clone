from django.urls import path, include
# from rest_framework import routers

# from . import api
from . import views

# router = routers.DefaultRouter()
# router.register(r'invoice', api.InvoiceViewSet)
# router.register(r'invoiceitem', api.InvoiceItemViewSet)
# router.register(r'Receive', api.ReceiveViewSet)


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
    path('invoice/pay/<int:pk>/', views.InvoicePayView.as_view(), name='sales_invoice_pay'),
)

urlpatterns += (
    # urls for InvoiceItem
    path('invoiceitem/', views.InvoiceItemListView.as_view(), name='sales_invoiceitem_list'),
    path('invoiceitem/create/', views.InvoiceItemCreateView.as_view(), name='sales_invoiceitem_create'),
    path('invoiceitem/detail/<int:pk>/', views.InvoiceItemDetailView.as_view(), name='sales_invoiceitem_detail'),
    path('invoiceitem/update/<int:pk>/', views.InvoiceItemUpdateView.as_view(), name='sales_invoiceitem_update'),
)

urlpatterns += (
    # urls for Receive
    path('receive/', views.ReceiveListView.as_view(), name='sales_receive_list'),
    path('receive/create/', views.ReceiveCreateView.as_view(), name='sales_receive_create'),
    path('receive/detail/<int:pk>/', views.ReceiveDetailView.as_view(), name='sales_receive_detail'),
    path('receive/update/<int:pk>/', views.ReceiveUpdateView.as_view(), name='sales_receive_update'),
)

