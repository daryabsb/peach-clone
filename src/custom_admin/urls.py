from django.urls import path
from . import views
from . import user_management

app_name = 'custom_admin'

urlpatterns = [
    path('', views.AdminDashboardView.as_view(), name='dashboard'),
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', views.AdminLogoutView.as_view(), name='logout'),
    
    # Company management
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/add/', views.CompanyCreateView.as_view(), name='company_add'),
    path('companies/<int:pk>/edit/', views.CompanyUpdateView.as_view(), name='company_edit'),
    path('companies/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),
    
    # Item management
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('items/add/', views.ItemCreateView.as_view(), name='item_add'),
    path('items/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_edit'),
    path('items/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
    
    # Invoice management
    path('invoices/', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/add/', views.InvoiceCreateView.as_view(), name='invoice_add'),
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),
    path('invoices/<int:pk>/edit/', views.InvoiceUpdateView.as_view(), name='invoice_edit'),
    path('invoices/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice_delete'),
    
    # Transaction management
    path('purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
    path('purchases/add/', views.PurchaseCreateView.as_view(), name='purchase_add'),
    path('purchases/<int:pk>/edit/', views.PurchaseUpdateView.as_view(), name='purchase_edit'),
    path('purchases/<int:pk>/delete/', views.PurchaseDeleteView.as_view(), name='purchase_delete'),
    
    path('sales/', views.SaleListView.as_view(), name='sale_list'),
    path('sales/add/', views.SaleCreateView.as_view(), name='sale_add'),
    path('sales/<int:pk>/edit/', views.SaleUpdateView.as_view(), name='sale_edit'),
    path('sales/<int:pk>/delete/', views.SaleDeleteView.as_view(), name='sale_delete'),
    
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/add/', views.PaymentCreateView.as_view(), name='payment_add'),
    path('payments/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment_edit'),
    path('payments/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),
    
    path('receives/', views.ReceiveListView.as_view(), name='receive_list'),
    path('receives/add/', views.ReceiveCreateView.as_view(), name='receive_add'),
    path('receives/<int:pk>/edit/', views.ReceiveUpdateView.as_view(), name='receive_edit'),
    path('receives/<int:pk>/delete/', views.ReceiveDeleteView.as_view(), name='receive_delete'),
    
    # User management
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/add/', views.UserCreateView.as_view(), name='user_add'),
    path('users/<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_edit'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    
    # Activity logs
    path('activity-logs/', views.AdminActivityListView.as_view(), name='activity_logs'),
    
    # User management
    path('users/', user_management.UserListView.as_view(), name='user_list'),
    path('users/add/', user_management.UserCreateView.as_view(), name='user_add'),
    path('users/<int:pk>/', user_management.UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/edit/', user_management.UserUpdateView.as_view(), name='user_edit'),
    path('users/<int:pk>/delete/', user_management.UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/reset-password/', user_management.UserPasswordResetView.as_view(), name='user_reset_password'),
]