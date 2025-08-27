from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import AdminActivity
from src.company.models import Company, Item
from src.transactions.models import Invoice, Purchase, Sale, Payment, Receive

User = get_user_model()

class CustomAdminTestCase(TestCase):
    def setUp(self):
        # Create a staff user for testing
        self.staff_user = User.objects.create_user(
            username='staffuser',
            email='staff@example.com',
            password='testpassword',
            is_staff=True
        )
        
        # Create a regular user for testing
        self.regular_user = User.objects.create_user(
            username='regularuser',
            email='regular@example.com',
            password='testpassword'
        )
        
        # Create test data
        self.company = Company.objects.create(
            name='Test Company',
            address='123 Test St',
            phone='1234567890',
            email='test@company.com'
        )
        
        self.item = Item.objects.create(
            name='Test Item',
            description='Test Description',
            company=self.company
        )
        
        # Create client
        self.client = Client()
    
    def test_login_view(self):
        # Test login with staff user
        response = self.client.post(reverse('custom_admin:login'), {
            'username': 'staffuser',
            'password': 'testpassword'
        })
        self.assertRedirects(response, reverse('custom_admin:dashboard'))
        
        # Check if login activity was logged
        self.assertTrue(AdminActivity.objects.filter(user=self.staff_user, action='login').exists())
        
        # Test login with regular user
        self.client.logout()
        response = self.client.post(reverse('custom_admin:login'), {
            'username': 'regularuser',
            'password': 'testpassword'
        })
        self.assertNotEqual(response.url, reverse('custom_admin:dashboard'))
    
    def test_logout_view(self):
        # Login first
        self.client.login(username='staffuser', password='testpassword')
        
        # Test logout
        response = self.client.get(reverse('custom_admin:logout'))
        self.assertRedirects(response, reverse('custom_admin:login'))
        
        # Check if logout activity was logged
        self.assertTrue(AdminActivity.objects.filter(user=self.staff_user, action='logout').exists())
    
    def test_dashboard_view(self):
        # Login as staff user
        self.client.login(username='staffuser', password='testpassword')
        
        # Test dashboard access
        response = self.client.get(reverse('custom_admin:dashboard'))
        self.assertEqual(response.status_code, 200)
        
        # Check context data
        self.assertEqual(response.context['company_count'], 1)
        self.assertEqual(response.context['user_count'], 2)  # staff_user and regular_user
        self.assertEqual(response.context['item_count'], 1)
        
        # Test dashboard access as regular user (should be denied)
        self.client.logout()
        self.client.login(username='regularuser', password='testpassword')
        response = self.client.get(reverse('custom_admin:dashboard'))
        self.assertNotEqual(response.status_code, 200)
    
    def test_company_views(self):
        # Login as staff user
        self.client.login(username='staffuser', password='testpassword')
        
        # Test company list view
        response = self.client.get(reverse('custom_admin:company_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Company')
        
        # Test company create view
        response = self.client.post(reverse('custom_admin:company_add'), {
            'name': 'New Company',
            'address': '456 New St',
            'phone': '0987654321',
            'email': 'new@company.com'
        })
        self.assertRedirects(response, reverse('custom_admin:company_list'))
        self.assertEqual(Company.objects.count(), 2)
    
    def test_item_views(self):
        # Login as staff user
        self.client.login(username='staffuser', password='testpassword')
        
        # Test item list view
        response = self.client.get(reverse('custom_admin:item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')
        
        # Test item create view
        response = self.client.post(reverse('custom_admin:item_add'), {
            'name': 'New Item',
            'description': 'New Description',
            'company': self.company.id
        })
        self.assertRedirects(response, reverse('custom_admin:item_list'))
        self.assertEqual(Item.objects.count(), 2)
    
    def test_ui_elements(self):
        # Login as staff user
        self.client.login(username='staffuser', password='testpassword')
        
        # Test dashboard UI elements
        response = self.client.get(reverse('custom_admin:dashboard'))
        
        # Check for stat cards
        self.assertContains(response, 'stat-card')
        
        # Check for financial summary
        self.assertContains(response, 'Financial Summary')
        
        # Check for transaction statistics
        self.assertContains(response, 'transactionChart')
        
        # Check for recent transactions
        self.assertContains(response, 'Recent Transactions')
        
        # Check for recent activities
        self.assertContains(response, 'Recent Activities')