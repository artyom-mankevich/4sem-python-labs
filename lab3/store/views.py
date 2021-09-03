import asyncio
import json

from django.conf.global_settings import LOGIN_URL
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from store.models import Product
from .forms import UserRegisterForm
from .utils import get_products, create_order, get_all_order_items, get_product, create_order_item, get_order


class IndexView(generic.TemplateView):
    template_name = 'store/index.html'


class ProductsView(LoginRequiredMixin, generic.ListView):
    template_name = 'store/all_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return all products"""
        return asyncio.run(get_products())


class ProductByIdView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = 'store/product.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}')
            return redirect('store:index')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})


def cart_data(request):
    user = request.user
    order, created = asyncio.run(create_order(user))
    items = asyncio.run(get_all_order_items(order))
    cart_items = order.items_count
    return {'cart_items': cart_items, 'order': order, 'items': items}


@login_required(login_url=LOGIN_URL)
def cart(request):
    data = cart_data(request)

    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'store/cart.html', context)


@login_required(login_url=LOGIN_URL)
def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    user = request.user
    product = asyncio.run(get_product(product_id))
    order, created = asyncio.run(create_order(user=user, complete=False))

    order_item, created = asyncio.run(create_order_item(order, product))

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        if order_item.quantity > 0:
            order_item.quantity -= 1
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)


@login_required(login_url=LOGIN_URL)
def save_order(request):
    data = json.loads(request.body)
    order_id = data['orderId']
    action = data['action']

    order = asyncio.run(get_order(order_id))

    if action == 'save':
        order.complete = True
        order.save()
        messages.success(request, 'Order successfully created')

    return HttpResponse(status=200)
