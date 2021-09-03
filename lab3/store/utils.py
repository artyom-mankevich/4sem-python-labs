from asgiref.sync import sync_to_async
from store.models import Product, Order, OrderItem


@sync_to_async
def get_products():
    return Product.objects.all()


@sync_to_async
def get_product(product_id):
    return Product.objects.get(id=product_id)


@sync_to_async
def create_order(user, complete=False):
    return Order.objects.get_or_create(user=user, complete=complete)


@sync_to_async
def create_order_item(order, product):
    return OrderItem.objects.get_or_create(order=order, product=product)


@sync_to_async
def get_order(pk):
    return Order.objects.get(pk=pk)


@sync_to_async
def get_all_order_items(order):
    return order.orderitem_set.all()



