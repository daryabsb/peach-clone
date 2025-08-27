from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from src.custom_admin.models import AdminPreference

User = get_user_model()

class Command(BaseCommand):
    help = 'Sets up initial admin users for the custom admin interface'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            type=str,
            help='Admin user email',
        )
        parser.add_argument(
            '--password',
            type=str,
            help='Admin user password',
        )
        parser.add_argument(
            '--name',
            type=str,
            help='Admin user name',
        )
    
    def handle(self, *args, **options):
        email = options.get('email')
        password = options.get('password')
        name = options.get('name')
        
        if not email:
            email = input('Enter admin email: ')
        
        if not password:
            password = input('Enter admin password: ')
            
        if not name:
            name = input('Enter admin name: ')
        
        try:
            with transaction.atomic():
                # Check if user already exists
                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={
                        'name': name,
                        'is_staff': True,
                        'is_active': True,
                    }
                )
                
                if created:
                    user.set_password(password)
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f'Admin user created: {email}'))
                else:
                    # Update existing user
                    user.name = name
                    user.is_staff = True
                    user.is_active = True
                    user.set_password(password)
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f'Admin user updated: {email}'))
                
                # Create admin preferences
                AdminPreference.objects.get_or_create(
                    user=user,
                    defaults={
                        'theme': 'light',
                        'sidebar_collapsed': False,
                        'items_per_page': 25
                    }
                )
                
                self.stdout.write(self.style.SUCCESS('Admin setup completed successfully'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error setting up admin: {str(e)}'))