from django.shortcuts import render, HttpResponse

from .models import Company, Owner, AccountMain

from django.views.generic import ListView, DetailView


class Home(ListView):
    model = Company
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['owners'] = Owner.objects.all()
        return context

def testjs(request):
    if request.POST:
        # de = []
        # for d in request.POST['desc']:
        print(request.POST)
        # print('posted')
        # print(request.POST)
    return render(request,'testjs.html', {})
