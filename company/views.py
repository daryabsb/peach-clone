from django.shortcuts import render
from django.db.models import Sum

from core.models import (
    Company,
    Owner,
    AccountMain,
    AccountSub,
    Item,
    Purchase,
    Customer,
    Vendor,
    Sale)

from django.views.generic import ListView, DetailView


class CompanyList(ListView):
    model = Company
    template_name = "company/company_list.html"

    # def get_queryset(self):
    #     queryset = Company.objects.
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['owners'] = Owner.objects.first()
        return context


class OwnerList(ListView):
    model = Owner
    template_name = "company/owners_list.html"


class AccountList(ListView):
    model = AccountMain
    template_name = "company/company_list.html"


class AccountList(ListView):
    model = AccountMain
    template_name = "company/company_list.html"


class AccountSubList(ListView):
    model = AccountSub
    template_name = "company/company_list.html"


class ItemList(ListView):
    model = Item
    template_name = "company/company_list.html"


class PurchaseList(ListView):
    model = Purchase
    template_name = "company/transactions_list.html"

    def get_queryset(self):
        # vendor = Vendor.objects.filter()
        vendor_list = Purchase.objects.all()
        return vendor_list

    def total_price(self):
        # vendor = 'Sham Computer'
        sub = Purchase.objects.all()
        total = sub.aggregate(Sum('total'))
        print(total)
        return total

    def get_context_data(self, **kwargs):
        # vendor = 'Sham Computer'
        context = super(PurchaseList, self).get_context_data()
        context['total_price'] = self.total_price()
        return context


class SaleList(ListView):
    model = Sale
    template_name = "company/transactions_list.html"

    def get_queryset(self):
        # vendor = 'Sham Computer'
        vendor_list = Sale.objects.all()
        return vendor_list

    def total_price(self):
        # vendor = 'Sham Computer'
        sub = Sale.objects.all()
        total = sub.aggregate(Sum('total'))
        print(total)
        return total

    def get_context_data(self, **kwargs):
        # vendor = 'Sham Computer'
        context = super(SaleList, self).get_context_data()
        context['total_price'] = self.total_price()
        return context
