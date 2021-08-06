from django.db import models


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.CharField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return ' '.join((str(self.id), self.first_name, self.second_name, self.email, self.phone_number))


class Order(models.Model):
    order_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join((str(self.id), str(self.user), str(self.order_date)))


class OrderItem(models.Model):
    quantity = models.IntegerField()
    unit_price = models.IntegerField("product price * quantity")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join((str(self.id), str(self.quantity), str(self.unit_price),
                         str(self.order), str(self.product)))


class Product(models.Model):
    category = models.CharField(max_length=250)
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    art_dating = models.CharField(max_length=250)
    art_id = models.CharField(max_length=50)
    artist = models.CharField(max_length=250)
    artist_birth = models.DateField()
    artist_death = models.DateField()
    artist_nationality = models.CharField(max_length=50)
    art_description = models.TextField(max_length=250)

    def __str__(self):
        return ' '.join((str(self.id), self.category, self.size,
                         self.price, self.title, self.art_dating,
                         self.art_id, self.artist))
