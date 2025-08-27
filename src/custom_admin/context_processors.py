from django.conf import settings
from django.urls import reverse
from .models import AdminPreference

def custom_admin_context(request):
    """Context processor for custom admin app"""
    context = {
        'custom_admin_site_header': getattr(settings, 'CUSTOM_ADMIN_SITE_HEADER', 'Peach Admin'),
        'custom_admin_site_title': getattr(settings, 'CUSTOM_ADMIN_SITE_TITLE', 'Peach Admin'),
        'custom_admin_index_title': getattr(settings, 'CUSTOM_ADMIN_INDEX_TITLE', 'Dashboard'),
        'custom_admin_base_url': getattr(settings, 'CUSTOM_ADMIN_BASE_URL', '/custom-admin/'),
    }
    
    # Add user preferences if user is authenticated
    if hasattr(request, 'user') and request.user.is_authenticated:
        try:
            preferences, created = AdminPreference.objects.get_or_create(
                user=request.user,
                defaults={
                    'theme': 'light',
                    'sidebar_collapsed': False,
                    'items_per_page': 25
                }
            )
            context['admin_preferences'] = preferences
        except Exception:
            # If there's an error, use default values
            context['admin_preferences'] = {
                'theme': 'light',
                'sidebar_collapsed': False,
                'items_per_page': 25
            }
    
    # Add navigation menu items
    context['admin_menu_items'] = [
        {
            'name': 'Dashboard',
            'url': reverse('custom_admin:dashboard'),
            'icon': 'fa-tachometer-alt',
        },
        {
            'name': 'Companies',
            'url': reverse('custom_admin:company_list'),
            'icon': 'fa-building',
        },
        {
            'name': 'Items',
            'url': reverse('custom_admin:item_list'),
            'icon': 'fa-box',
        },
        {
            'name': 'Invoices',
            'url': reverse('custom_admin:invoice_list'),
            'icon': 'fa-file-invoice',
        },
        {
            'name': 'Purchases',
            'url': reverse('custom_admin:purchase_list'),
            'icon': 'fa-shopping-cart',
        },
        {
            'name': 'Sales',
            'url': reverse('custom_admin:sale_list'),
            'icon': 'fa-cash-register',
        },
        {
            'name': 'Payments',
            'url': reverse('custom_admin:payment_list'),
            'icon': 'fa-money-bill-wave',
        },
        {
            'name': 'Receives',
            'url': reverse('custom_admin:receive_list'),
            'icon': 'fa-hand-holding-usd',
        },
        {
            'name': 'Users',
            'url': reverse('custom_admin:user_list'),
            'icon': 'fa-users',
        },
        {
            'name': 'Activity Log',
            'url': reverse('custom_admin:activity_log'),
            'icon': 'fa-history',
        },
    ]
    
    return context