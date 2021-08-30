import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'username, email, first_name, last_name,'
    ' password1, password2, status_code',
    [
        # correct info: should be redirected to index
        ('billy', 'billy@gym.com', '', '', 'bossofthegym', 'bossofthegym', 302),
        # incorrect_info: should reload the page
        ('^^^^', 'billy@gym.com', '', '', 'bossofthegym', 'bossofthegym', 200),
    ]
)
@pytest.mark.django_db
def test_register_view(client, username, email, first_name,
                       last_name, password1, password2, status_code):
    response = client.post(
        reverse('store:register'),
        data={
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password1': password1,
            'password2': password2,
        },
    )
    assert response.status_code == status_code


def test_index_view(client):
    url = reverse('store:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_products_view_anon(client):
    path = reverse('store:products')
    response = client.get(path)
    assert response.status_code == 302


@pytest.mark.django_db
def test_products_view_auth(client, user_factory):
    user = user_factory()
    client.force_login(user)
    path = reverse('store:products')
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_id_view_anon(client, product_factory):
    product = product_factory()
    path = reverse('store:product by id', kwargs={'pk': product.id})
    response = client.get(path)
    assert response.status_code == 302


@pytest.mark.django_db
def test_product_id_view_auth(client, user_factory, product_factory):
    user = user_factory()
    client.force_login(user)
    product = product_factory()
    path = reverse('store:product by id', kwargs={'pk': product.id})
    response = client.get(path)
    assert response.status_code == 200
