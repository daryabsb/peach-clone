from django.shortcuts import render
from django.db.models import Sum

from src.company.models import (
    Company,
    # Owner,
   )

from django.views.generic import ListView, DetailView


class CompanyList(ListView):
    model = Company
    # template_name = "company/company_list.html"

    # def get_queryset(self):
    #     queryset = Company.objects.
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['owners'] = Owner.objects.first()
        return context


# class OwnerList(ListView):
#     model = Owner
#     template_name = "company/owners_list.html"


# class AccountList(ListView):
#     model = AccountMain
#     template_name = "company/company_list.html"


# class AccountList(ListView):
#     model = AccountMain
#     template_name = "company/company_list.html"


# class AccountSubList(ListView):
#     model = AccountSub
#     template_name = "company/company_list.html"


# class ItemList(ListView):
#     model = Item
#     template_name = "company/company_list.html"
