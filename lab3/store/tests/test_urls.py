from django.urls import reverse, resolve


def test_index_url():
    path = reverse('store:index')
    assert resolve(path).view_name == 'store:index'


def test_products_url():
    path = reverse('store:products')
    assert resolve(path).view_name == 'store:products'


def test_product_id_url():
    path = reverse('store:product by id', kwargs={'pk': 1})
    assert resolve(path).view_name == 'store:product by id'


def test_register_url():
    path = reverse('store:register')
    assert resolve(path).view_name == 'store:register'


def test_cart_url():
    path = reverse('store:cart')
    assert resolve(path).view_name == 'store:cart'


def test_update_item_url():
    path = reverse('store:update_item')
    assert resolve(path).view_name == 'store:update_item'


def test_save_order_url():
    path = reverse('store:save_order')
    assert resolve(path).view_name == 'store:save_order'
