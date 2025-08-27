from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class AdminPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin to check if the user has admin permissions.
    Requires the user to be authenticated and have staff status.
    """
    permission_denied_message = "You do not have permission to access the admin area."
    login_url = None
    
    def get_login_url(self):
        return reverse('custom_admin:login')
    
    def test_func(self):
        # Check if the user is authenticated and has staff status
        if not self.request.user.is_authenticated:
            return False
        
        # Check if admin permission is required in settings
        if getattr(settings, 'CUSTOM_ADMIN_PERMISSION_REQUIRED', True):
            return self.request.user.is_staff
        
        return True
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.permission_denied_message)
            return redirect('accounts:dashboard')
        return super().handle_no_permission()


class ModelPermissionMixin(AdminPermissionMixin):
    """
    Mixin to check if the user has permission to perform actions on a specific model.
    Extends AdminPermissionMixin to first check admin access.
    
    Subclasses should define:
    - model_name: The name of the model (e.g., 'company', 'item')
    - action: The action being performed ('view', 'add', 'change', 'delete')
    """
    model_name = None
    action = None
    
    def test_func(self):
        # First check admin permission
        if not super().test_func():
            return False
        
        # If no specific model permission is required, allow access
        if not self.model_name or not self.action:
            return True
        
        # Check for specific model permission
        # This is a simplified implementation - in a real app, you might use Django's permission system
        # or implement a more sophisticated permission model
        
        # Example: Check if user has permission for this model and action
        # permission_codename = f'{self.action}_{self.model_name}'
        # return self.request.user.has_perm(f'app_name.{permission_codename}')
        
        # For now, we'll just allow staff users to do everything
        return self.request.user.is_staff


class ViewPermissionMixin(ModelPermissionMixin):
    """Mixin for view permissions"""
    action = 'view'


class AddPermissionMixin(ModelPermissionMixin):
    """Mixin for add permissions"""
    action = 'add'


class ChangePermissionMixin(ModelPermissionMixin):
    """Mixin for change permissions"""
    action = 'change'


class DeletePermissionMixin(ModelPermissionMixin):
    """Mixin for delete permissions"""
    action = 'delete'