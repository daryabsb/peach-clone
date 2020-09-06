from django.shortcuts import render

from .models import Company

from django.views.generic import ListView, DetailView


class Home(ListView):
    model = Company
    template_name = "index.html"