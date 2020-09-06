from django.shortcuts import render

from core.models import Company

from django.views.generic import ListView, DetailView


class CompanyList(ListView):
    model = Company
    template_name = "company/company_list.html"

    # def get_queryset(self):
    #     queryset = Company.objects.