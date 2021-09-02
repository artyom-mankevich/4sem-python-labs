from pytest_factoryboy import register

from store.tests.factories import ProductFactory, UserFactory, OrderFactory, OrderItemFactory

register(UserFactory)
register(ProductFactory)
register(OrderFactory)
register(OrderItemFactory)
