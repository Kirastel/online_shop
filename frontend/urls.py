from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('categories', views.categories, name='categories'),
    path('categories/<slug>', views.categories_product, name='categories_list'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('product/<product_id>', views.product, name='product'),
    path('add/<product_id>', views.cart_add, name='cart_add'),
    path('clear', views.cart_clear, name='cart_clear'),
]
