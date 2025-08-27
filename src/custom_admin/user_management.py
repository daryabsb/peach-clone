from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from src.accounts.models import User
from .models import AdminActivity
from .permissions import AdminPermissionMixin, ViewPermissionMixin, AddPermissionMixin, ChangePermissionMixin, DeletePermissionMixin


class UserListView(ViewPermissionMixin, ListView):
    """View for listing all users"""
    model = User
    template_name = 'custom_admin/user_list.html'
    context_object_name = 'users'
    paginate_by = 10
    model_name = 'user'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        
        if search_query:
            queryset = queryset.filter(
                email__icontains=search_query
            ) | queryset.filter(
                first_name__icontains=search_query
            ) | queryset.filter(
                last_name__icontains=search_query
            )
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['active_users'] = User.objects.filter(is_active=True).count()
        context['inactive_users'] = User.objects.filter(is_active=False).count()
        context['staff_users'] = User.objects.filter(is_staff=True).count()
        return context


class UserDetailView(ViewPermissionMixin, DetailView):
    """View for viewing user details"""
    model = User
    template_name = 'custom_admin/user_detail.html'
    context_object_name = 'user_obj'  # Use user_obj to avoid conflict with request.user
    model_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        
        # Get user activities
        context['activities'] = AdminActivity.objects.filter(user=user).order_by('-timestamp')[:10]
        
        # Log the view activity
        AdminActivity.objects.create(
            user=self.request.user,
            action='viewed',
            content_type='user',
            object_id=user.id,
            ip_address=self.get_client_ip(),
            url=self.request.path,
            method=self.request.method
        )
        
        return context
    
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip


class UserCreateView(AddPermissionMixin, CreateView):
    """View for creating a new user"""
    model = User
    template_name = 'custom_admin/user_form.html'
    fields = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    success_url = reverse_lazy('custom_admin:user_list')
    model_name = 'user'
    
    def form_valid(self, form):
        # Set a default password for the user
        user = form.save(commit=False)
        user.set_password('changeme')  # Default password that user should change
        response = super().form_valid(form)
        
        # Log the create activity
        AdminActivity.objects.create(
            user=self.request.user,
            action='created',
            content_type='user',
            object_id=user.id,
            ip_address=self.get_client_ip(),
            url=self.request.path,
            method=self.request.method
        )
        
        messages.success(self.request, f"User {user.email} created successfully. Default password is 'changeme'.")
        return response
    
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip


class UserUpdateView(ChangePermissionMixin, UpdateView):
    """View for updating a user"""
    model = User
    template_name = 'custom_admin/user_form.html'
    fields = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    context_object_name = 'user_obj'  # Use user_obj to avoid conflict with request.user
    model_name = 'user'
    
    def get_success_url(self):
        return reverse_lazy('custom_admin:user_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        
        # Log the update activity
        AdminActivity.objects.create(
            user=self.request.user,
            action='updated',
            content_type='user',
            object_id=user.id,
            ip_address=self.get_client_ip(),
            url=self.request.path,
            method=self.request.method
        )
        
        messages.success(self.request, f"User {user.email} updated successfully.")
        return response
    
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip


class UserDeleteView(DeletePermissionMixin, DeleteView):
    """View for deleting a user"""
    model = User
    template_name = 'custom_admin/user_confirm_delete.html'
    success_url = reverse_lazy('custom_admin:user_list')
    context_object_name = 'user_obj'  # Use user_obj to avoid conflict with request.user
    model_name = 'user'
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        
        # Don't allow deleting yourself
        if user == request.user:
            messages.error(request, "You cannot delete your own account.")
            return redirect('custom_admin:user_detail', pk=user.pk)
        
        # Log the delete activity before deleting
        AdminActivity.objects.create(
            user=self.request.user,
            action='deleted',
            content_type='user',
            object_id=user.id,
            ip_address=self.get_client_ip(),
            url=self.request.path,
            method=self.request.method
        )
        
        messages.success(request, f"User {user.email} deleted successfully.")
        return super().delete(request, *args, **kwargs)
    
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip


class UserPasswordResetView(ChangePermissionMixin, UpdateView):
    """View for resetting a user's password"""
    model = User
    template_name = 'custom_admin/user_password_reset.html'
    fields = []  # No fields needed as we're just resetting the password
    context_object_name = 'user_obj'  # Use user_obj to avoid conflict with request.user
    model_name = 'user'
    
    def get_success_url(self):
        return reverse_lazy('custom_admin:user_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        user = self.object
        user.set_password('changeme')  # Reset to default password
        user.save()
        
        # Log the password reset activity
        AdminActivity.objects.create(
            user=self.request.user,
            action='reset_password',
            content_type='user',
            object_id=user.id,
            ip_address=self.get_client_ip(),
            url=self.request.path,
            method=self.request.method
        )
        
        messages.success(self.request, f"Password for {user.email} has been reset to 'changeme'.")
        return redirect(self.get_success_url())
    
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip