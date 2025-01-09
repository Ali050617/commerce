from django.shortcuts import render, get_object_or_404, redirect
from .models import Checkout
from products.models import Product


def checkout_list(request):
    checkouts = Checkout.objects.all()
    return render(request, 'index.html', {'checkouts': checkouts})


def checkout_detail(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    return render(request, 'detail.html', {'checkout': checkout})


def checkout_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        card_number = request.POST.get('card_number')
        date = request.POST.get('date')
        cvv = request.POST.get('cvv')
        product_ids = request.POST.getlist('products')
        if (first_name and last_name and
                email and address and city
                and zip_code and card_number
                and date and cvv and product_ids):
            checkout = Checkout.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=address,
                city=city,
                zip_code=zip_code,
                card_number=card_number,
                date=date,
                cvv=cvv,
            )
            checkout.products.set(Product.objects.filter(id=product_ids))
            return redirect('checkout_list')
    return render(request, 'checkout.html')
