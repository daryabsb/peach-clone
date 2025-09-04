

menu_list = ['Companies', 'Transactions', 'Finances', 'Statements','Reports', 'Settings']
menu_items_list = {
    'Companies': ['Company', 'Item'],
    'Transactions': ['Invoice', 'Purchase', 'Payment', 'Receive'],
    'Finances': ['Sales', 'Purchases'],
    'Statements': ['Balance Sheet', 'Income Statement', 'Cash Flow Statement'],
    'Reports': ['Quarterly Report', 'Annual Report', 'Inventory'],
    'Settings': ['Company Settings', 'User Settings'],


}
MENU_INITIAL_DATA = [
    {'title': 'Companies', 'access_level': 2},
    {'title': 'Transactions', 'access_level': 2},
    {'title': 'Finances', 'access_level': 2},
    {'title': 'Statements', 'access_level': 2},
    {'title': 'Reports', 'access_level': 2},
    {'title': 'Settings', 'access_level': 2},
]

from django.utils.text import slugify
MENU_ITEMS_INITIAL_DATA = [
    {'menu_slug': slugify(menu), 'title': item, 'link': f'/{slugify(item)}/', 'order': idx}
    for menu, items in menu_items_list.items()
    for idx, item in enumerate(items, 1)
]