from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from products.models import Product


def cart_detail(request, id):
    cart = get_object_or_404(Cart, id=id)
    return render(request, 'detail.html', {'cart': cart})


def cart_create(request, cart_id, product_id):
    cart = get_object_or_404(Cart, id=cart_id)
    product = get_object_or_404(Product, id=product_id)
    cart.products.add(product)
    cart.update_total()
    return redirect('cart_detail', id=cart.id)


def cart_remove_product(request, cart_id, product_id):
    cart = get_object_or_404(Cart, id=cart_id)
    product = get_object_or_404(Product, id=product_id)
    cart.products.remove(product)
    cart.update_total()
    return redirect('cart_detail', id=cart.id)
