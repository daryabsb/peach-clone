from django.shortcuts import render
# from django.db.models import Sum

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# from .forms import PurchaseForm, SaleForm, PaymentForm, ReceiveForm, InvoiceForm

from core.models import (
    Company, Owner, AccountMain, Item, Customer,
    Vendor, Purchase, Sale, Payment,
    Receive, Invoice, IncomeStatement,)

from django.views.generic import ListView, DetailView


class IncomeStatementView(ListView):
    model = IncomeStatement
    template_name = 'statements.html'
