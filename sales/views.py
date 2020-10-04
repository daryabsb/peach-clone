from django.shortcuts import render, HttpResponseRedirect
# Create your views here.
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from core.models import Invoice, InvoiceItem, Receive, Customer
from .forms import InvoiceForm, InvoiceItemForm, InvoiceItemFormSet, ReceiveForm


class InvoiceListView(ListView):
    model = Invoice

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    
    # success_url = f'sales/update/')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoiceitem_form = InvoiceItemFormSet()
        
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  invoiceitem_form=invoiceitem_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoiceitem_form = InvoiceItemFormSet(self.request.POST)

        if (form.is_valid() and invoiceitem_form.is_valid()):
            return self.form_valid(form, invoiceitem_form)
        else:
            return self.form_invalid(form, invoiceitem_form)

    def form_valid(self, form, invoiceitem_form):
        self.object = form.save()
        invoiceitem_form.instance = self.object
        invoiceitem_form.save()

        return HttpResponseRedirect(self.get_success_url())
        # return self.render_to_response(
        #     self.get_context_data(form=form,
        #                           invoiceitem_form=invoiceitem_form))

    def form_invalid(self, form, invoiceitem_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  invoiceitem_form=invoiceitem_form))


class InvoiceDetailView(DetailView):
    model = Invoice

    def get_context_data(self, *args, **kwargs):
        context = super(InvoiceDetailView, self).get_context_data()
        print(context)
        items = InvoiceItem.objects.filter(invoice=self.kwargs['pk'])
        context['items'] = items
        # for item in items:
        #     print(item.item)
        return context


class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm

    def get(self, request, *args, **kwargs):
        
        invoice = Invoice.objects.get(id=kwargs['pk'])
        print(invoice)
        self.object = invoice
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoiceitem_form = InvoiceItemFormSet(instance=invoice)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  invoiceitem_form=invoiceitem_form))

    def post(self, request, *args, **kwargs):
        invoice = Invoice.objects.get(id=kwargs['pk'])
        self.object = invoice
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoiceitem_form = InvoiceItemFormSet(self.request.POST)

        if (form.is_valid() and invoiceitem_form.is_valid()):
            return self.form_valid(form, invoiceitem_form)
        else:
            return self.form_invalid(form, invoiceitem_form)

    def form_valid(self, form, invoiceitem_form):
        self.object = form.save(commit=False)
        invoiceitem_form.instance = self.object
        invoiceitem_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, invoiceitem_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  invoiceitem_form=invoiceitem_form))


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


class InvoicePayView(CreateView):
    model = Receive
    form_class = ReceiveForm


    def get_context_data(self, *args, **kwargs):
        context = super(InvoicePayView, self).get_context_data(*args, **kwargs)
        invoice = Invoice.objects.get(id=self.kwargs['pk'])
        customers = Customer.objects.exclude(id=invoice.customer.id)
        invoices = Invoice.objects.exclude(id=invoice.id)
        # form = self.get_form_class(initial={'invoice':19})
        context['invoice'] = invoice
        context['invoices'] = invoices
        context['customers'] = customers
        context['amount'] = invoice.balance

        print(context)
        return context

class ReceiveListView(ListView):
    model = Receive


class ReceiveCreateView(CreateView):
    model = Receive
    form_class = ReceiveForm


class ReceiveDetailView(DetailView):
    model = Receive


class ReceiveUpdateView(UpdateView):
    model = Receive
    form_class = ReceiveForm
