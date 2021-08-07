from django.contrib import admin

# Register your models here.
from store.models import *

admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)