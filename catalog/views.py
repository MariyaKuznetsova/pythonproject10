from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View

from catalog.forms import ProductForm
from catalog.models import Product
from catalog.services import get_products_by_category


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        product.unpublish = request.POST.get("is_publication")
        product.save()

        return redirect("catalog:product_detail", pk=product_id)


class DeleteProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm("catalog.can_delete_product"):
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        product.delete()

        return redirect("catalog:product_list")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_category = context['products'][0].category
        context["category"] = get_products_by_category(product_category)
        return context

    def get_queryset(self):
        queryset = cache.get("products_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("products_queryset", queryset, 60)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = "catalog.product_delete"
    success_url = reverse_lazy("catalog:product_list")
    context_object_name = "product"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.owner == self.request.user:
            return HttpResponseForbidden("У вас нет прав для удаление этого продукта")
        return obj
