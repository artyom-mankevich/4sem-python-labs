from django.contrib import admin

# Register your models here.
from store.models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 5


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'order_date', 'complete', 'total_price']}),
    ]
    inlines = [OrderItemInline]
    list_display = ('id', 'user', 'order_date', 'total_price')


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Art Info', {'fields': ['title', 'category', 'price',
                                 'size', 'art_id', 'art_dating',
                                 'art_description']}),
        ('Artist Info', {'fields': ['artist', 'artist_nationality',
                                    'artist_birth', 'artist_death']})
    ]
    list_display = ('id', 'title', 'category', 'artist', 'price', 'size', 'art_id')
    list_filter = ['category', 'artist', 'price', 'size']
    search_fields = ['id', 'title', 'art_id']


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)