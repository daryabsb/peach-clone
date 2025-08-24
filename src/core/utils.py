import random
import ast
from src.settings.components.env import config
from collections import OrderedDict


def recursive_to_dict(obj):
    if isinstance(obj, list):
        return [recursive_to_dict(item) for item in obj]
    elif isinstance(obj, OrderedDict):
        return {key: recursive_to_dict(value) for key, value in obj.items()}
    else:
        return obj


def generate_cache_key(base_name, user=None, warehouse=None, customer=None):
    parts = [base_name]

    if user and not (user.is_staff or user.is_superuser):
        parts.append(f"user_{user.id}")

    if warehouse:
        parts.append(
            f"warehouse_{warehouse.id if hasattr(warehouse, 'id') else warehouse}")

    if customer:
        parts.append(
            f"customer_{customer.id if hasattr(customer, 'id') else customer}")

    return "_".join(parts)


# def get_columns(app_name, fields=None, qs=None, actions=False):
#     from src.configurations.models import AppTableColumn
#     if not qs:
#         qs = AppTableColumn.objects.filter(
#             is_enabled=True, app__name=app_name
#         )
#     if fields:
#         qs = qs.filter(name__in=fields)

#     columns = [
#         {
#             "id": index,
#             "data": column.related_value if column.is_related else column.name,
#             "name": column.name,
#             "title": column.title,
#             "searchable": column.searchable,
#             "orderable": column.orderable,
#         } for index, column in enumerate(qs)
#     ]
#     if actions:
#         columns.append({
#             "id": len(columns) + 1,
#             "data": 'actions',
#             "name": 'actions',
#             "title": 'Actions',
#             "searchable": False,
#             "orderable": False,
#         })
#     return columns


# def get_indexes(app_name, qs=None, fields=None, actions=None):
#     from src.configurations.models import AppTableColumn

#     if not qs:
#         qs = AppTableColumn.objects.filter(
#             is_enabled=True, app__name=app_name
#         )
#     if fields:
#         qs = qs.filter(name__in=fields)

#     indexes = {column.name: index for index, column in enumerate(qs)}
#     if app_name == 'documents':
#         indexes['product'] = len(indexes)
#     indexes['start_date'] = len(indexes)
#     indexes['end_date'] = len(indexes)
#     if actions:
#         indexes['actions'] = len(indexes)
#     return indexes


# def get_fields(app_name, fields=None):
#     from src.configurations.models import AppTableColumn
#     queryset = AppTableColumn.objects.filter(
#         is_enabled=True, app__name=app_name
#     )
#     if fields:
#         queryset = queryset.filter(name__in=fields)
#     return [column.related_value if column.is_related else column.name for column in queryset]


# def get_searchable_fields(app_name, fields=None, actions=False):
#     from src.configurations.models import AppTableColumn
#     queryset = AppTableColumn.objects.filter(
#         is_enabled=True, app__name=app_name, searchable=True
#     )

#     indexes = get_indexes(app_name, fields=fields,
#                           qs=queryset, actions=actions)
#     columns = get_columns(app_name, fields=fields,
#                           qs=queryset, actions=actions)
#     fields = get_fields(app_name, fields=fields)

#     return fields, columns, indexes


def generate_number(target=None, code=''):
    from datetime import date
    min = 100
    max = 3999
    digits = str(random.randint(min, max))
    digits = (len(str(max))-len(digits))*'0'+digits

    if not target:
        target = 'order'
    # print(request.user.id)
    # print(date.today().strftime("%A %d. %B %Y"))
    # print(date.today().strftime("%d%m%Y"))

    if code:
        code = f'{code}-'

    return f'{target}-{code}{date.today().strftime("%d%m%Y")}-{digits}'


def generate_ean13():
    from src.products.models import Barcode
    while True:
        ean = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        checksum = calculate_ean13_checksum(ean)
        ean13 = ean + str(checksum)
        if not Barcode.objects.filter(value=ean13).exists():
            print(ean13)
            return ean13

# For configuration model


def convert_value(value):
    try:
        # Attempt to evaluate the value to its original type
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        # If evaluation fails, return the value as-is (it is a string)
        return value


def calculate_ean13_checksum(ean):
    # Calculate the checksum for the EAN-13 barcode
    sum_odd = sum(int(ean[i]) for i in range(0, 12, 2))
    sum_even = sum(int(ean[i]) for i in range(1, 12, 2))
    checksum = (10 - (sum_odd + sum_even * 3) % 10) % 10
    return checksum


def slugify_function(content):
    return content.replace('_', '-').lower()


def add_spaces(input_string):
    spaced_string = ''
    for i, char in enumerate(input_string):
        spaced_string += char
        if (i + 1) % 4 == 0 and i != len(input_string) - 1:
            spaced_string += ' '
    return spaced_string


def remove_spaces(input_string):
    return input_string.replace(' ', '')


def has_spaces(input_string):
    return ' ' in input_string


def hungary_notation(text):
    """
    驼峰表示法 -> 匈牙利表示法

    :param text:
    :return:
    """
    import re
    text_list = list(text)
    for m in sorted((re.finditer('[A-Z]', text)), key=(lambda x: x.span()), reverse=True):
        text_list[m.start():m.end()] = '_' + str(m.group()).lower()

    formatted = ''.join(text_list).strip('_')
    return formatted


def remove_duplicate_elements(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not x in seen if not seen_add(x)]


def get_args_form_dict(key, _dict, expect_type, default=None):
    value = _dict.get(key, default)
    if not isinstance(value, expect_type):
        if not isinstance(default, expect_type):
            value = expect_type()
        else:
            value = default
    return value


def get_num_from_list(a_list):
    container = []
    for item in a_list:
        try:
            container.append(int(item))
        except ValueError:
            pass

    if not container:
        container.append(0)
    return container
