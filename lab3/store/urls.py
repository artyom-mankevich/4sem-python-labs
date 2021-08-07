from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    # ex: /store/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /store/products/
    path('products/', views.ProductsView.as_view(), name='products'),
    # ex: /store/products/5
    path('products/<int:pk>', views.ProductByIdView.as_view(), name='product by id')
]
