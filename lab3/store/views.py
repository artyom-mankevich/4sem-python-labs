from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic

from store.models import Product


class IndexView(generic.TemplateView):
    template_name = 'store/index.html'


class ProductsView(generic.ListView):
    template_name = 'store/all_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return all products"""
        return Product.objects.all()


class ProductByIdView(generic.DetailView):
    model = Product
    template_name = 'store/product.html'


def product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product.html', {'product': product})
