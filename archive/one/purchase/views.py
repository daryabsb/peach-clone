from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Invoice, InvoiceItem, Payment
from .forms import InvoiceForm, InvoiceItemForm, PaymentForm


class InvoiceListView(ListView):
    model = Invoice


class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm


class InvoiceDetailView(DetailView):
    model = Invoice


class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm


class InvoiceItemListView(ListView):
    model = InvoiceItem


class InvoiceItemCreateView(CreateView):
    model = InvoiceItem
    form_class = InvoiceItemForm


class InvoiceItemDetailView(DetailView):
    model = InvoiceItem


class InvoiceItemUpdateView(UpdateView):
    model = InvoiceItem
    form_class = InvoiceItemForm


class PaymentListView(ListView):
    model = Payment


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm


class PaymentDetailView(DetailView):
    model = Payment


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm

