from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

