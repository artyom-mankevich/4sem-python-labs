import pytest


@pytest.mark.django_db
def test_product_str(product_factory):
    product = product_factory()
    expected = f'{product.id} {product.category} {product.size} {product.price} {product.title} {product.art_dating}' \
               f' {product.art_id} {product.artist}'
    assert expected == str(product)
