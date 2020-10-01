from django.shortcuts import render, redirect
from django.db.models import Sum

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.forms import inlineformset_factory

from .forms import (
    PurchaseForm, SaleForm, PaymentForm, ReceiveForm, 
    InvoiceForm, InvoiceCreateForm,)

from core.models import (
    Company, Owner, AccountMain, Item, Customer,
    Vendor, Purchase, Sale, Payment,
    Receive, Invoice, InvoiceItem)

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

class InvoiceDetail(DetailView):
    model = Invoice
    template_name = 'transactions/invoice_detail.html'

    def get_context_data(self, **kwargs):
        # vendor = 'Sham Computer'
        context = super(InvoiceDetail, self).get_context_data()
        
        print(context)
        context['model_name'] = 'Invoice'
        return context

class CreateInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    # fields = 'department'
    template_name = 'transactions/create_invoice_item.html'
    success_url = '/transactions/invoices'

    def form_valid(self, form):

        # print(form)
        return super().form_valid(form)
    
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise forms.ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['urlr'] = f"url 'transactions:invoice-add'"
        return context


from django.http import HttpResponseRedirect


def create_invoice(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = InvoiceCreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/transactions/invoices/<pk:pk>/add')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InvoiceCreateForm()

    return render(request, 'transactions/create_invoice2.html', {'form': form})


def add_invoice_items(request, pk):
    # if this is a POST request we need to process the form data
    # print(invoice_id)
    invoice = Invoice.objects.get(pk=pk)
    # invoice_items_formset = inlineformset_factory(Invoice, InvoiceItem, fields='__all__')
    
    if request.method == 'POST':
        formset = invoice_items_formset(request.POST, instance=invoice)

        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = InvoiceForm(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            formset.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('/transactions/invoices/')

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = InvoiceForm()

    return render(request, 'transactions/invoice_detail.html', {})