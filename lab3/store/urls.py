from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductByIdView.as_view(), name='product by id'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.update_item, name='update_item'),
    path('save_order/', views.save_order, name='save_order')
]
