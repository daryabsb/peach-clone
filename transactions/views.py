from django.shortcuts import render
from django.db.models import Sum

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import PurchaseForm, SaleForm, PaymentForm, ReceiveForm

from core.models import (
    Company,
    Owner,
    AccountMain,
    AccountSub,
    Item,
    Purchase,
    Customer,
    Vendor,
    Sale,
    Payment,
    Receive)

from django.views.generic import ListView, DetailView


class PurchaseList(ListView):
    model = Purchase
    template_name = "transactions.html"

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
        context['model_name'] = 'Purchase'
        return context


class SaleList(ListView):
    model = Sale
    template_name = "transactions.html"

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
        context['model_name'] = 'Sale'
        return context


class PaymentList(ListView):
    model = Payment
    template_name = "transactions.html"

    def get_queryset(self):
        # vendor = 'Sham Computer'
        payment_list = Payment.objects.all()
        return payment_list

    def total_price(self):
        # vendor = 'Sham Computer'
        sub = Payment.objects.all()
        total = sub.aggregate(Sum('amount'))
        print(total)
        return total

    def get_context_data(self, **kwargs):
        # vendor = 'Sham Computer'
        context = super(PaymentList, self).get_context_data()
        context['total_price'] = self.total_price()
        context['model_name'] = 'Payment'
        return context


class ReceiveList(ListView):
    model = Receive
    template_name = "transactions.html"

    def get_queryset(self):
        # vendor = 'Sham Computer'
        receive_list = Receive.objects.all()
        return receive_list

    def total_price(self):
        # vendor = 'Sham Computer'
        sub = Receive.objects.all()
        total = sub.aggregate(Sum('amount'))
        print(total)
        return total

    def get_context_data(self, **kwargs):
        # vendor = 'Sham Computer'
        context = super(ReceiveList, self).get_context_data()
        context['total_price'] = self.total_price()
        context['model_name'] = 'Receive'
        return context





class CreatePurchase(CreateView):
    model = Purchase
    form_class = PurchaseForm
    # fields = 'department'
    template_name = 'transactions/create_transaction.html'
    success_url = '/transactions/purchases'

class CreateSale(CreateView):
    model = Sale
    form_class = SaleForm
    # fields = 'department'
    template_name = 'transactions/create_transaction.html'
    success_url = '/transactions/sales'

class CreatePayment(CreateView):
    model = Payment
    form_class = PaymentForm
    # fields = 'department'
    template_name = 'transactions/create_transaction.html'
    success_url = '/transactions/payments'

class CreateReceive(CreateView):
    model = Receive
    form_class = ReceiveForm
    # fields = 'department'
    template_name = 'transactions/create_transaction.html'
    success_url = '/transactions/receives'
    
