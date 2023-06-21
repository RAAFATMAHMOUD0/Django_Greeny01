from django.shortcuts import render
from django.views.generic import ListView, DateDetailView
from .models import Product


class ProductList(ListView):
    model = Product


class ProductDateil(DateDetailView):
    model = Product