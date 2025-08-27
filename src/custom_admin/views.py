from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum, Count
from django.utils import timezone

from src.accounts.models import User, Customer, Vendor
from src.company.models import Company, Item
from src.transactions.models import Invoice, Purchase, Sale, Payment, Receive, Journal
from .models import AdminActivity
from .forms import (
    CustomAdminAuthForm, CompanyAdminForm, ItemAdminForm, InvoiceAdminForm,
    PurchaseAdminForm, SaleAdminForm, PaymentAdminForm, ReceiveAdminForm
)


from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views import View

class AdminLoginView(View):
    """Custom admin login view"""
    template_name = 'custom_admin/login.html'
    form_class = CustomAdminAuthForm
    redirect_authenticated_user = True
    
    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Redirect authenticated users to the admin dashboard
        if self.redirect_authenticated_user and request.user.is_authenticated:
            if request.user.is_staff:
                return redirect(reverse_lazy('custom_admin:dashboard'))
            else:
                messages.warning(request, "You don't have permission to access the admin area.")
                return redirect('accounts:dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Log the login activity
            AdminActivity.objects.create(
                user=user,
                action='login',
                ip_address=self.get_client_ip(request),
                url=request.path,
                method=request.method
            )
            
            # Redirect to the admin dashboard if the user is staff
            if user.is_staff:
                messages.success(request, f"Welcome back, {user.get_full_name() or user.username}!")
                return redirect(reverse_lazy('custom_admin:dashboard'))
            else:
                messages.warning(request, "You don't have permission to access the admin area.")
                logout(request)
                return redirect('accounts:dashboard')
        
        return render(request, self.template_name, {'form': form})
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class AdminLogoutView(View):
    """Custom admin logout view"""
    
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Log the logout activity
            AdminActivity.objects.create(
                user=request.user,
                action='logout',
                ip_address=self.get_client_ip(request),
                url=request.path,
                method=request.method
            )
            
            # Logout the user
            logout(request)
            messages.success(request, "You have been successfully logged out.")
        
        return redirect(reverse_lazy('custom_admin:login'))
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


from .permissions import AdminPermissionMixin, ViewPermissionMixin, AddPermissionMixin, ChangePermissionMixin, DeletePermissionMixin

# Use our new permission mixin instead of the simple one
class AdminRequiredMixin(AdminPermissionMixin):
    """Mixin to ensure user is authenticated and is staff"""
    pass


class AdminDashboardView(AdminRequiredMixin, TemplateView):
    """Admin dashboard view"""
    template_name = 'custom_admin/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import datetime
        
        # Get counts for various models
        context['company_count'] = Company.objects.count()
        context['user_count'] = User.objects.count()
        context['customer_count'] = Customer.objects.count()
        context['vendor_count'] = Vendor.objects.count()
        context['item_count'] = Item.objects.count()
        
        # Get transaction counts
        context['invoice_count'] = Invoice.objects.count()
        context['purchase_count'] = Purchase.objects.count()
        context['sale_count'] = Sale.objects.count()
        context['payment_count'] = Payment.objects.count()
        context['receive_count'] = Receive.objects.count()
        
        # Calculate total transactions for percentage calculations
        context['total_transactions'] = (
            context['invoice_count'] + 
            context['purchase_count'] + 
            context['sale_count'] + 
            context['payment_count'] + 
            context['receive_count']
        ) or 1  # Avoid division by zero
        
        # Get active vs inactive counts
        context['active_users'] = User.objects.filter(is_active=True).count()
        context['inactive_users'] = User.objects.filter(is_active=False).count()
        
        # Get recent activities
        context['recent_activities'] = AdminActivity.objects.select_related('user').order_by('-timestamp')[:10]
        
        # Get financial summary
        today = timezone.now().date()
        start_of_month = datetime.date(today.year, today.month, 1)
        
        # Today's financial data
        context['sales_today'] = Sale.objects.filter(created__date=today).aggregate(total=Sum('total'))['total'] or 0
        context['purchases_today'] = Purchase.objects.filter(created__date=today).aggregate(total=Sum('total'))['total'] or 0
        
        # This month's financial data
        context['sales_this_month'] = Sale.objects.filter(created__date__gte=start_of_month).aggregate(total=Sum('total'))['total'] or 0
        context['purchases_this_month'] = Purchase.objects.filter(created__date__gte=start_of_month).aggregate(total=Sum('total'))['total'] or 0
        
        # Recent transactions
        context['recent_sales'] = Sale.objects.order_by('-created')[:5]
        context['recent_purchases'] = Purchase.objects.order_by('-created')[:5]
        context['recent_payments'] = Payment.objects.order_by('-created')[:5]
        context['recent_receives'] = Receive.objects.order_by('-created')[:5]
        
        return context


# Company Views
class CompanyListView(AdminRequiredMixin, ListView):
    """List view for companies"""
    model = Company
    template_name = 'custom_admin/company/list.html'
    context_object_name = 'companies'


class CompanyCreateView(AdminRequiredMixin, CreateView):
    """Create view for companies"""
    model = Company
    form_class = CompanyAdminForm
    template_name = 'custom_admin/company/form.html'
    success_url = reverse_lazy('custom_admin:company_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created company: {form.instance.title}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Company "{form.instance.title}" created successfully')
        return response


class CompanyUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for companies"""
    model = Company
    form_class = CompanyAdminForm
    template_name = 'custom_admin/company/form.html'
    success_url = reverse_lazy('custom_admin:company_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated company: {form.instance.title}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Company "{form.instance.title}" updated successfully')
        return response


class CompanyDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for companies"""
    model = Company
    template_name = 'custom_admin/company/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:company_list')
    
    def delete(self, request, *args, **kwargs):
        company = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted company: {company.title}',
            content_type=None,
            object_id=company.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'Company "{company.title}" deleted successfully')
        return response


# Item Views
class ItemListView(AdminRequiredMixin, ListView):
    """List view for items"""
    model = Item
    template_name = 'custom_admin/item/list.html'
    context_object_name = 'items'


class ItemCreateView(AdminRequiredMixin, CreateView):
    """Create view for items"""
    model = Item
    form_class = ItemAdminForm
    template_name = 'custom_admin/item/form.html'
    success_url = reverse_lazy('custom_admin:item_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created item: {form.instance.name}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Item "{form.instance.name}" created successfully')
        return response


class ItemUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for items"""
    model = Item
    form_class = ItemAdminForm
    template_name = 'custom_admin/item/form.html'
    success_url = reverse_lazy('custom_admin:item_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated item: {form.instance.name}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Item "{form.instance.name}" updated successfully')
        return response


class ItemDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for items"""
    model = Item
    template_name = 'custom_admin/item/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:item_list')
    
    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted item: {item.name}',
            content_type=None,
            object_id=item.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'Item "{item.name}" deleted successfully')
        return response


# Invoice Views
class InvoiceListView(AdminRequiredMixin, ListView):
    """List view for invoices"""
    model = Invoice
    template_name = 'custom_admin/invoice/list.html'
    context_object_name = 'invoices'


class InvoiceDetailView(AdminRequiredMixin, DetailView):
    """Detail view for invoices"""
    model = Invoice
    template_name = 'custom_admin/invoice/detail.html'
    context_object_name = 'invoice'


class InvoiceCreateView(AdminRequiredMixin, CreateView):
    """Create view for invoices"""
    model = Invoice
    form_class = InvoiceAdminForm
    template_name = 'custom_admin/invoice/form.html'
    success_url = reverse_lazy('custom_admin:invoice_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created invoice: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Invoice #{form.instance.id} created successfully')
        return response


class InvoiceUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for invoices"""
    model = Invoice
    form_class = InvoiceAdminForm
    template_name = 'custom_admin/invoice/form.html'
    success_url = reverse_lazy('custom_admin:invoice_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated invoice: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Invoice #{form.instance.id} updated successfully')
        return response


class InvoiceDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for invoices"""
    model = Invoice
    template_name = 'custom_admin/invoice/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:invoice_list')
    
    def delete(self, request, *args, **kwargs):
        invoice = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted invoice: {invoice.id}',
            content_type=None,
            object_id=invoice.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'Invoice #{invoice.id} deleted successfully')
        return response


# Purchase Views
class PurchaseListView(AdminRequiredMixin, ListView):
    """List view for purchases"""
    model = Purchase
    template_name = 'custom_admin/purchase/list.html'
    context_object_name = 'purchases'


class PurchaseCreateView(AdminRequiredMixin, CreateView):
    """Create view for purchases"""
    model = Purchase
    form_class = PurchaseAdminForm
    template_name = 'custom_admin/purchase/form.html'
    success_url = reverse_lazy('custom_admin:purchase_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created purchase: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Purchase #{form.instance.id} created successfully')
        return response


class PurchaseUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for purchases"""
    model = Purchase
    form_class = PurchaseAdminForm
    template_name = 'custom_admin/purchase/form.html'
    success_url = reverse_lazy('custom_admin:purchase_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated purchase: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Purchase #{form.instance.id} updated successfully')
        return response


class PurchaseDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for purchases"""
    model = Purchase
    template_name = 'custom_admin/purchase/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:purchase_list')
    
    def delete(self, request, *args, **kwargs):
        purchase = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted purchase: {purchase.id}',
            content_type=None,
            object_id=purchase.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'Purchase #{purchase.id} deleted successfully')
        return response


# Sale Views
class SaleListView(AdminRequiredMixin, ListView):
    """List view for sales"""
    model = Sale
    template_name = 'custom_admin/sale/list.html'
    context_object_name = 'sales'


class SaleCreateView(AdminRequiredMixin, CreateView):
    """Create view for sales"""
    model = Sale
    form_class = SaleAdminForm
    template_name = 'custom_admin/sale/form.html'
    success_url = reverse_lazy('custom_admin:sale_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created sale: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Sale #{form.instance.id} created successfully')
        return response


class SaleUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for sales"""
    model = Sale
    form_class = SaleAdminForm
    template_name = 'custom_admin/sale/form.html'
    success_url = reverse_lazy('custom_admin:sale_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated sale: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Sale #{form.instance.id} updated successfully')
        return response


class SaleDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for sales"""
    model = Sale
    template_name = 'custom_admin/sale/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:sale_list')
    
    def delete(self, request, *args, **kwargs):
        sale = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted sale: {sale.id}',
            content_type=None,
            object_id=sale.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'Sale #{sale.id} deleted successfully')
        return response


# Payment Views
class PaymentListView(AdminRequiredMixin, ListView):
    """List view for payments"""
    model = Payment
    template_name = 'custom_admin/payment/list.html'
    context_object_name = 'payments'


class PaymentCreateView(AdminRequiredMixin, CreateView):
    """Create view for payments"""
    model = Payment
    form_class = PaymentAdminForm
    template_name = 'custom_admin/payment/form.html'
    success_url = reverse_lazy('custom_admin:payment_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created payment: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Payment #{form.instance.id} created successfully')
        return response


class PaymentUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for payments"""
    model = Payment
    form_class = PaymentAdminForm
    template_name = 'custom_admin/payment/form.html'
    success_url = reverse_lazy('custom_admin:payment_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated payment: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Payment #{form.instance.id} updated successfully')
        return response


class PaymentDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for payments"""
    model = Payment
    template_name = 'custom_admin/payment/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:payment_list')
    
    def delete(self, request, *args, **kwargs):
        payment = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted payment: {payment.id}',
            content_type=None,
            object_id=payment.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'Payment #{payment.id} deleted successfully')
        return response


# Receive Views
class ReceiveListView(AdminRequiredMixin, ListView):
    """List view for receives"""
    model = Receive
    template_name = 'custom_admin/receive/list.html'
    context_object_name = 'receives'


class ReceiveCreateView(AdminRequiredMixin, CreateView):
    """Create view for receives"""
    model = Receive
    form_class = ReceiveAdminForm
    template_name = 'custom_admin/receive/form.html'
    success_url = reverse_lazy('custom_admin:receive_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created receive: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Receive #{form.instance.id} created successfully')
        return response


class ReceiveUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for receives"""
    model = Receive
    form_class = ReceiveAdminForm
    template_name = 'custom_admin/receive/form.html'
    success_url = reverse_lazy('custom_admin:receive_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated receive: {form.instance.id}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'Receive #{form.instance.id} updated successfully')
        return response


class ReceiveDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for receives"""
    model = Receive
    template_name = 'custom_admin/receive/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:receive_list')
    
    def delete(self, request, *args, **kwargs):
        receive = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted receive: {receive.id}',
            content_type=None,
            object_id=receive.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'Receive #{receive.id} deleted successfully')
        return response


# User Views
class UserListView(AdminRequiredMixin, ListView):
    """List view for users"""
    model = User
    template_name = 'custom_admin/user/list.html'
    context_object_name = 'users'


class UserCreateView(AdminRequiredMixin, CreateView):
    """Create view for users"""
    model = User
    fields = ['email', 'name', 'is_active', 'is_staff']
    template_name = 'custom_admin/user/form.html'
    success_url = reverse_lazy('custom_admin:user_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Created user: {form.instance.email}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'User "{form.instance.email}" created successfully')
        return response


class UserUpdateView(AdminRequiredMixin, UpdateView):
    """Update view for users"""
    model = User
    fields = ['email', 'name', 'is_active', 'is_staff']
    template_name = 'custom_admin/user/form.html'
    success_url = reverse_lazy('custom_admin:user_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Updated user: {form.instance.email}',
            content_type=None,
            object_id=form.instance.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(self.request, f'User "{form.instance.email}" updated successfully')
        return response


class UserDeleteView(AdminRequiredMixin, DeleteView):
    """Delete view for users"""
    model = User
    template_name = 'custom_admin/user/confirm_delete.html'
    success_url = reverse_lazy('custom_admin:user_list')
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        response = super().delete(request, *args, **kwargs)
        
        # Log activity
        AdminActivity.objects.create(
            user=self.request.user,
            action=f'Deleted user: {user.email}',
            content_type=None,
            object_id=user.id,
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f'User "{user.email}" deleted successfully')
        return response


# Activity Log Views
class AdminActivityListView(AdminRequiredMixin, ListView):
    """List view for admin activities"""
    model = AdminActivity
    template_name = 'custom_admin/activity/list.html'
    context_object_name = 'activities'
    ordering = ['-timestamp']
    paginate_by = 50