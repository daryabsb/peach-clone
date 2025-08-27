from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .models import AdminActivity


class AdminLoginView(View):
    """Custom admin login view"""
    template_name = 'custom_admin/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    
    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Redirect authenticated users to the admin dashboard
        if self.redirect_authenticated_user and request.user.is_authenticated:
            if request.user.is_staff:
                return redirect(reverse('custom_admin:dashboard'))
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
                return redirect(reverse('custom_admin:dashboard'))
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
        
        return redirect(reverse('custom_admin:login'))
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip