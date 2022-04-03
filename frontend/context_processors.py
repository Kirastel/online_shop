from .cart import Cart
from products.models import Categories


def cart(request):
    return {'cart': Cart(request)}


def category_list(request):
    return {'category_list': Categories.objects.all()}
