from django.shortcuts import render
from django.db.models import Sum

from .forms import DateForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# from .forms import PurchaseForm, SaleForm, PaymentForm, ReceiveForm, InvoiceForm

from core.models import (
    Company, Owner, AccountMain, Item, Customer,
    Vendor, Purchase, Sale, Payment,
    Receive, Invoice, IncomeStatement, Journal,)

from django.views.generic import ListView, DetailView

from datetime import timedelta


class IncomeStatementView(ListView):
    model = Journal
    form_class = DateForm()
    template_name = 'statements.html'
    template_name = 'dashgrin/statements2.html'

    def get_queryset(self):

        return Journal.objects.filter(dr_account__title='Sale Revenue')

    def get_revenue(self):
        # print(request)
        # revenue = Journal.objects.all().aggregate(sum('amount'))
        date_start = self.request.GET.get('date-start')
        date_end = self.request.GET.get('date-end')
        print(f'{date_start} till {date_end}')
        queryset = super(IncomeStatementView, self).get_queryset().filter(
            created__range=[date_start, date_end])
        print(queryset)
        revenue = queryset.aggregate(Sum('amount'))

        return revenue

    def get_context_data(self, *args, **kwargs):
        context = super(IncomeStatementView, self).get_context_data(
            *args, **kwargs)

        revenue = self.get_revenue()
    #     for inc in context:
    #         if inc.dr_account.title == 'Sale Revenue':
    #             income.append(inc)
        context['revenue'] = revenue

        return context
