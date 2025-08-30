from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from django.urls import resolve
from asgiref.sync import sync_to_async
from django.contrib.contenttypes.models import ContentType
from .models import AdminActivity
import re

class AdminActivityMiddleware(MiddlewareMixin):
    """Middleware to track admin user activities"""
    
    def __init__(self, get_response):
        self.get_response = get_response
        # Patterns to exclude from tracking
        self.exclude_patterns = [
            r'^/custom-admin/login/$',
            r'^/custom-admin/logout/$',
            r'^/static/.*$',
            r'^/media/.*$',
        ]

    def __call__(self, request):
        return self.get_response(request)

    async def __call__(self, request):
        return await self.get_response(request)
    
    def should_track(self, path):
        """Check if the request path should be tracked"""
        for pattern in self.exclude_patterns:
            if re.match(pattern, path):
                return False
        return path.startswith('/custom-admin/')
    
    async def process_view(self, request, view_func, view_args, view_kwargs):
        """Process the view and log activity if needed"""
        if not self.should_track(request.path):
            return None
            
        if isinstance(request.user, AnonymousUser) or not request.user.is_authenticated:
            return None
            
        # Get the resolved URL name
        try:
            resolver_match = await sync_to_async(resolve)(request.path)
            url_name = resolver_match.url_name
            namespace = resolver_match.namespace
            
            # Determine the action based on the URL pattern
            action = 'viewed'
            if url_name:
                if 'add' in url_name or 'create' in url_name:
                    action = 'created'
                elif 'edit' in url_name or 'update' in url_name:
                    action = 'updated'
                elif 'delete' in url_name:
                    action = 'deleted'
            
            # Get content type and object ID if available
            content_type = None
            object_id = None
            
            # Try to extract model name from URL name
            model_name = None
            if url_name:
                parts = url_name.split('_')
                if len(parts) > 1:
                    model_name = parts[0]
            
            # If we have a model name and an ID in kwargs, get the content type
            if model_name and 'pk' in view_kwargs:
                try:
                    # This is a simplified approach - in a real app you might need a mapping
                    app_models = {
                        'company': 'company',
                        'item': 'company',
                        'invoice': 'transactions',
                        'purchase': 'transactions',
                        'sale': 'transactions',
                        'payment': 'transactions',
                        'receive': 'transactions',
                        'user': 'accounts',
                    }
                    
                    if model_name in app_models:
                        app_label = app_models[model_name]
                        content_type = await sync_to_async(ContentType.objects.get)(app_label=app_label, model=model_name)
                        object_id = view_kwargs['pk']
                except (ContentType.DoesNotExist, KeyError):
                    pass
            
            # Log the activity
            await sync_to_async(AdminActivity.objects.create)(
                user=request.user,
                action=action,
                content_type=content_type,
                object_id=object_id,
                ip_address=self.get_client_ip(request),
                url=request.path,
                method=request.method
            )
            
        except Exception as e:
            # Log the error but don't interrupt the request
            print(f"Error logging admin activity: {e}")
            
        return None
    
    def get_client_ip(self, request):
        """Get the client IP address from the request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip