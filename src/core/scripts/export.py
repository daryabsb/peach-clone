from core.models import (
    AccountMain, AccountSub, Address, Company, Owner,
    Customer, DSP, Invoice, Item, Vendor
)
from django.forms import model_to_dict
from decimal import Decimal


def run():
    accounts = Vendor.objects.all()
    account_list = []
    for account in accounts:
        account_dict = model_to_dict(account)
        account_list.append(account_dict)
    print(account_list)

account_mains = [
    {'id': 1, 'title': 'Fixed Assets', 'description': 'bbb', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 1, 'company': 2, 'account_section': 'Assets'}, 
    {'id': 7, 'title': 'Non Fixed Assets', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 7, 'company': 1, 'account_section': 'Assets'}, 
    {'id': 9, 'title': 'Operating Revenues', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 9, 'company': 1, 'account_section': 'Revenue'}, 
    {'id': 10, 'title': 'Operating Expenses', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 10, 'company': 1, 'account_section': 'Expense'}, 
    {'id': 11, 'title': 'Current Liabilities', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 11, 'company': 1, 'account_section': 'Liabilities'}, 
    {'id': 13, 'title': 'Intangibile Assets', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 13, 'company': 1, 'account_section': 'Assets'}, 
    {'id': 25, 'title': 'Fixed Liabilities', 'description': 'All of the long term and fixed liabilities', 'dr': Decimal('0.00'), 
    'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 25, 'company': 1, 'account_section': 'Liabilities'}, 
    {'id': 26, 'title': 'Owners Equity', 'description': 'All of the accounts of equity', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 
    'balance': Decimal('0.00'), 'accounttemplate_ptr': 26, 'company': 1, 'account_section': 'Equity'}, 
    {'id': 27, 'title': 'Non Operating Revenues', 'description': 'all of the revenues that are outside the framework of the company', 
    'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 27, 'company': 1, 'account_section': 
    'Revenue'}, 
    {'id': 28, 'title': 'Non operating Expenses', 'description': 'all of the expenses that are outside the framework of the company', 
    'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 28, 'company': 1, 
    'account_section': 'Expense'}
]

account_subs = [
    {'id': 2, 'title': 'Inventory', 'description': 'inv', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 2, 'main': 7}, 
    {'id': 8, 'title': 'Equipments', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 8, 'main': 1}, 
    {'id': 14, 'title': 'Sale Revenue', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('3039600.02'), 
    'accounttemplate_ptr': 14, 'main': 9}, 
    {'id': 15, 'title': 'Account Payable', 'description': '', 'dr': Decimal('-11463.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 15, 'main': 11}, 
    {'id': 16, 'title': 'Account Receivable', 'description': '', 'dr': Decimal('3030256.02'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 16, 'main': 7}, 
    {'id': 17, 'title': 'Rent', 'description': '', 'dr': Decimal('500.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 17, 'main': 10}, 
    {'id': 20, 'title': 'Cash', 'description': '', 'dr': Decimal('-2307.00'), 'cr': Decimal('3700.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 20, 'main': 7}, 
    {'id': 21, 'title': 'Unearned Revenue', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('300.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 21, 'main': 11}, 
    {'id': 22, 'title': 'Prepaid Expenses', 'description': '', 'dr': Decimal('6000.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 22, 'main': 7}, 
    {'id': 29, 'title': 'Supplies', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 29, 'main': 7}, 
    {'id': 30, 'title': 'Supplies Expense', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 30, 'main': 10}, 
    {'id': 31, 'title': 'Land', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 31, 'main': 1}, 
    {'id': 32, 'title': 'Buildings', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 32, 'main': 1}, 
    {'id': 33, 'title': 'Wages Payable', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 33, 'main': 11}, 
    {'id': 34, 'title': 'Interest Payable', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 34, 'main': 11}, 
    {'id': 35, 'title': 'Taxes Payable', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 35, 'main': 11}, 
    {'id': 36, 'title': 'Income Tax', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 36, 'main': 10}, 
    {'id': 37, 'title': 'Bonds payable', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 37, 'main': 25}, 
    {'id': 38, 'title': 'Retained Earnings', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 38, 'main': 26}, 
    {'id': 39, 'title': 'Withdrawals', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 39, 'main': 26}, 
    {'id': 40, 'title': 'Salaries', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 40, 'main': 10}, 
    {'id': 41, 'title': 'Utilities', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 41, 'main': 10}, 
    {'id': 42, 'title': 'Other operating Expenses', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 42, 'main': 10}, 
    {'id': 43, 'title': 'Interest expense', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 43, 'main': 10}, 
    {'id': 44, 'title': 'Insurance Expense', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 44, 'main': 10}, 
    {'id': 45, 'title': 'Depreciation Expense', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 45, 'main': 10}, 
    {'id': 46, 'title': 'Service Revenue', 'description': '', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 
    'accounttemplate_ptr': 46, 'main': 9}
]

addresses = [
    {'id': 1, 'addr_line1': 'Raparrin, Pashacity', 'city': 'Slemani', 'state': 'Kurdistan', 'country': 'Iraq', 'zipcode': '46001', 
    'phone': '07701570615', 'email': 'info@fig-plus.com'}
    ]

owners = [{'id': 1, 'name': 'Rand', 'share': Decimal('0.99')}]

companies = [
    {'id': 1, 'user': 1, 'title': 'Imperial Knight', 'parent_company': None, 'description': 'IK', 
    'address':1, 'account_type': 'accrual', 'owners': [1]}, 
    {'id': 2, 'user': 1, 'title': 'Fig Quality Technology', 'parent_company': 1, 'description': 'Fig', 
    'address': 1, 'account_type': 'accrual', 'owners': [1]}, 
    {'id': 3, 'user': 1, 'title': 'Lox Agency for Quality Control', 'parent_company': 1, 'description': 'Lox', 
    'address': 1, 'account_type': 'accrual', 'owners': [1]}
]

customers = [
    {'id': 1, 'name': 'Kogay Shar', 'address': 1, 'phone': '07701570615', 'balance': Decimal('2395.02'), 'cvbase_ptr': 1, 'account_type': 16}, 
    {'id': 2, 'name': 'Balen Pharmacy', 'address': 1, 'phone': '07701570615', 'balance': Decimal('3003543.00'), 'cvbase_ptr': 7, 'account_type': 16}, 
    {'id': 3, 'name': 'Dalya Market', 'address': 1, 'phone': '+9647701570615', 'balance': Decimal('30429.00'), 'cvbase_ptr': 10, 'account_type': 16}
]

vendors = [
    {'name': 'Sham Computer',   'phone': '07701570615', 'balance': Decimal('0.00'), 'account_type': 15}, 
    {'name': 'Big Power',       'phone': '07701570615', 'balance': Decimal('0.00'), 'account_type': 15}, 
    {'name': 'Diwan Furniture', 'phone': '07701570615', 'balance': Decimal('0.00'), 'account_type': 15}, 
    {'name': 'Mamosta Falah',   'phone': '07701570615', 'balance': Decimal('0.00'), 'account_type': 15}, 
    {'name': 'IQ Network',      'phone': '07701570615', 'balance': Decimal('0.00'), 'account_type': 15}, 
    {'name': 'Baharan Complex', 'phone': '07701570615', 'balance': Decimal('0.00'), 'account_type': 17}, 
    {'name': 'Dara Qadir',      'phone': '07701570615', 'balance': Decimal('0.00'), 'account_type': 15}
]

dsps = [
    {'id': 1, 'title': 'End of the World', 'depreciation_choices': 1, 'lifespan': 5}, 
    {'id': 2, 'title': 'Only iMac 5years', 'depreciation_choices': 1, 'lifespan': 5}
]

items = [
    {'title': 'Mask Blue',  'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 3, 'account_sub': 14, 'item_depretiation': 1}, 
    {'title': 'Laptop',     'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 4, 'account_sub': 8, 'item_depretiation': 1}, 
    {'title': 'UPS',        'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 5, 'account_sub': 2, 'item_depretiation': 1}, 
    {'title': 'iPhone X',   'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 6, 'account_sub': 8, 'item_depretiation': 1}, 
    {'title': 'Store rent', 'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 18, 'account_sub': 17, 'item_depretiation': 1}, 
    {'title': 'Computer',   'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 19, 'account_sub': 8, 'item_depretiation': 1}, 
    {'title': 'Internet',   'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 23, 'account_sub': 22, 'item_depretiation': 1}, 
    {'title': 'Desk',       'dr': Decimal('0.00'), 'cr': Decimal('0.00'), 'balance': Decimal('0.00'), 'accounttemplate_ptr': 24, 'account_sub': 8, 'item_depretiation': 1}
]
