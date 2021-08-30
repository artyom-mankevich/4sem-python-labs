import datetime

import pytest

from store.models import Product


@pytest.mark.django_db
def test_product_str(product_factory):
    product = product_factory()
    expected = f'{id} {product.category} {product.size} {product.price} {product.title} {product.art_dating} {product.art_id} {product.artist}'
    assert expected == str(product)
