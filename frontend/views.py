from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from products.models import Product
from orders.models import ProductInOrder
from .cart import Cart
from .forms import CartAddProductForm, CheckoutForm, ContactForm


def index(request):
    products = Product.objects.filter(availability='In stock').select_related('type')
    context = {
        'products': products,
    }
    return render(request, 'frontend/index.html', context=context)


def categories(request):
    products = get_list_or_404(Product.objects.order_by('append_date').filter(is_active=True))

    context = {
        'products': products,
    }
    return render(request, 'frontend/categories.html', context=context)


def categories_product(request, slug):
    products = get_list_or_404(
        Product.objects
            .order_by('append_date')
            .filter(is_active=True, type__slug=slug)
            .select_related('type')
            .defer('availability', 'short_description', 'description')
    )

    context = {
        'products': products,
    }
    return render(request, 'frontend/categories.html', context=context)


def product(request, product_id):
    product = get_object_or_404(
        Product.objects
            .filter(id=product_id)
            .select_related('type')
    )
    cart_product_form = CartAddProductForm()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'frontend/product.html', context=context)


def checkout(request):
    cart = Cart(request)
    checkout_form = CheckoutForm(request.POST)

    if request.method == 'POST':
        if checkout_form.is_valid():
            order = checkout_form.save()
            for item in cart:
                ProductInOrder.objects.create(order=order,
                                              product_order=item['product'],
                                              price=item['price'],
                                              number=item['quantity'])
            cart.clear()
            return redirect('categories')
    else:
        checkout_form = CheckoutForm()
    context = {
        'cart': cart,
        'checkout_form': checkout_form
    }
    return render(request, 'frontend/checkout.html', context=context)


def contact(request):
    contact_form = ContactForm(request.POST)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()

            return redirect('index')
    else:
        contact_form = ContactForm()

        return render(request, 'frontend/contact.html', {'form': contact_form})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    product = get_object_or_404(
        Product.objects
            .filter(id=product_id)
            .select_related('type')
    )
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    return redirect('product', product_id=product.id)


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')


def cart(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'frontend/cart.html', context=context)
