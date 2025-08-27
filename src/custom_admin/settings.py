from django.conf import settings

# Custom Admin Settings
CUSTOM_ADMIN_SITE_HEADER = "Peach Admin"
CUSTOM_ADMIN_SITE_TITLE = "Peach Admin Portal"
CUSTOM_ADMIN_INDEX_TITLE = "Welcome to Peach Admin"

# Custom Admin Permissions
CUSTOM_ADMIN_PERMISSION_REQUIRED = 'is_staff'

# Custom Admin Templates
CUSTOM_ADMIN_BASE_TEMPLATE = 'custom_admin/base.html'
CUSTOM_ADMIN_LOGIN_TEMPLATE = 'custom_admin/login.html'
CUSTOM_ADMIN_DASHBOARD_TEMPLATE = 'custom_admin/dashboard.html'

# Custom Admin URLs
CUSTOM_ADMIN_URL = 'custom-admin/'

# Custom Admin Pagination
CUSTOM_ADMIN_ITEMS_PER_PAGE = 20