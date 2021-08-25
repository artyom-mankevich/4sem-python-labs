from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def get_cart_total_price(self):
        order_items = self.orderitem_set.all()
        self.total_price = sum([item.get_total for item in order_items])
        return self.total_price

    @property
    def items_count(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def __str__(self):
        return ' '.join((f'ID: {str(self.id)};', f'UserID: {str(self.user.id)};',
                         f'OrderDate: {str(self.order_date)}'))


class OrderItem(models.Model):
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    @property
    def get_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return ' '.join((f'ID: {str(self.id)};', str(self.order.id),
                         str(self.quantity), str(self.product)))


class Product(models.Model):
    category = models.CharField(max_length=250)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    title = models.CharField(max_length=250)
    art_dating = models.CharField(max_length=250)
    art_id = models.CharField(max_length=50)
    artist = models.CharField(max_length=250)
    artist_birth = models.DateField()
    artist_death = models.DateField()
    artist_nationality = models.CharField(max_length=50)
    art_description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return ' '.join((str(self.id), self.category, self.size,
                         str(self.price), self.title, self.art_dating,
                         self.art_id, self.artist))
