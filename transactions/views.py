from django.shortcuts import render
from django.db.models import Sum

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import PurchaseForm, SaleForm, PaymentForm, ReceiveForm, InvoiceForm

from core.models import (
    Company, Owner, AccountMain, Item, Customer,
    Vendor, Purchase, Sale, Payment,
    Receive, Invoice,)

from django.views.generic import ListView, DetailView

class CustomerSaleView(ListView):
    title = 'Customer and Sales'
    template_name = "revenues.html"
    model = None


    def get_queryset(self):
        return Sale.objects.all()

    def get_context_data(self):
        context = super(CustomerSaleView, self).get_context_data()
        # context['sales'] = Sale.objects.all()
        context['secondary'] = Customer.objects.all()
        context['model_main'] = 'Sale'
        context['model_secondary'] = 'Customer'
        return context

class VendorPurchaseView(ListView):
    title = 'Vendor and Purchasess'
    template_name = "revenues.html"
    model = None


    def get_queryset(self):
        return Purchase.objects.all()

    def get_context_data(self):
        context = super(VendorPurchaseView, self).get_context_data()
        # context['sales'] = Sale.objects.all()
        context['secondary'] = Vendor.objects.all()
        context['model_main'] = 'Purchase'
        context['model_secondary'] = 'Vendor'
        return context


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
        invoices = Invoice.objects.filter(customer__name='Kogay Shar')
        print(invoices)
        context = super(SaleList, self).get_context_data()
        context['total_price'] = self.total_price()
        context['model_name'] = 'Sale'
        context['invoices'] = invoices
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


class InvoiceList(ListView):
    title = 'Invoice List'
    model = Invoice      # shorthand for setting queryset = models.Car.objects.all()
    template_name = 'transactions.html'

    def get_context_data(self, **kwargs):
        # vendor = 'Sham Computer'
        context = super(InvoiceList, self).get_context_data()
        context['model_name'] = 'Invoice'
        return context


class CreateInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    # fields = 'department'
    template_name = 'transactions/create_invoice.html'
    success_url = '/transactions/invoices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['urlr'] = f"url 'transactions:invoice-add'"
        return context
