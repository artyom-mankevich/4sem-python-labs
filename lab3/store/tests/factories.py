import datetime

import factory
from django.contrib.auth.models import User

from store.models import Product, Order, OrderItem


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'johny'
    email = 'johny@mail.com'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    category = "Poster"
    size = "24\" x 18\""
    price = "29.99"
    title = "Self-portrait"
    art_dating = "1887"
    art_id = "SK-A-3262",
    artist = "Vincent van Gogh"
    artist_birth = "1853-03-30"
    artist_death = "1890-07-29"
    artist_nationality = "Nederlands"
    art_description = "Vincent moved to Paris in 1886, after hearing from his brother Theo "
    "about the new, colourful style of French painting. Wasting no time, "
    "he tried it out in several self-portraits. He did this mostly to "
    "avoid having to pay for a model. Using rhythmic brushstrokes in "
    "striking colours, he portrayed himself here as a fashionably dressed "
    "Parisian."


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    order_date = datetime.datetime.now()
    user = factory.SubFactory(UserFactory)
    complete = False
    total_price = 29.99


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    quantity = 1
    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
