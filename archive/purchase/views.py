from django.views.generic import DetailView, ListView, UpdateView, CreateView
from core.models import PurchaseInvoice, Purchase, Payment
from .forms import PurchaseInvoiceForm, PurchaseInvoiceItemForm, PaymentForm, PurchaseInvoiceItemFormSet


class PurchaseInvoiceListView(ListView):
    model = PurchaseInvoice


class PurchaseInvoiceCreateView(CreateView):
    model = PurchaseInvoice
    form_class = PurchaseInvoiceForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoiceitem_form = PurchaseInvoiceItemFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  invoiceitem_form=invoiceitem_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # print(form.is_valid())
        invoiceitem_form = PurchaseInvoiceItemFormSet(self.request.POST)

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


class PurchaseInvoiceDetailView(DetailView):
    model = PurchaseInvoice


class PurchaseInvoiceUpdateView(UpdateView):
    model = PurchaseInvoice
    form_class = PurchaseInvoiceForm


class PurchaseInvoiceItemListView(ListView):
    model = Purchase


class PurchaseInvoiceItemCreateView(CreateView):
    model = Purchase
    form_class = PurchaseInvoiceItemForm


class PurchaseInvoiceItemDetailView(DetailView):
    model = Purchase


class PurchaseInvoiceItemUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseInvoiceItemForm


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

