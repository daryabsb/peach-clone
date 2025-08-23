from src.company.models import Company, Owner, Address
from src.accounts.models import User


companies = [
    {'id': 1, 'user': 1, 'title': 'Imperial Knight', 'parent_company': None, 'description': 'IK', 
    'address':1, 'account_type': 'accrual', 'owners': [1]}, 
    {'id': 2, 'user': 1, 'title': 'Fig Quality Technology', 'parent_company': 1, 'description': 'Fig', 
    'address': 1, 'account_type': 'accrual', 'owners': [1]}, 
    {'id': 3, 'user': 1, 'title': 'Lox Agency for Quality Control', 'parent_company': 1, 'description': 'Lox', 
    'address': 1, 'account_type': 'accrual', 'owners': [1]}
]

def run():
    for company in companies:
        # Company.objects.create(**company)
        user = User.objects.first()
        address=Address.objects.first()
        owners = Owner.objects.all()
        parent_company = None
        if Company.objects.exists() and company['parent_company']:
            parent_company = Company.objects.get(id=company['parent_company'])
        
        company_obj = Company(
            # owners=owners.set(), 
            id=company['id'],
            user=user, 
            address=address,
            title="company['title']",
            parent_company=parent_company,
            description="company['description']",
            account_type="company['account_type']"
            )
        for owner in owners:
            company_obj.owners.add(owner)
        
        company_obj.save()
        

            
