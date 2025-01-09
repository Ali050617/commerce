from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category


def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request,year, month, day, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    return render(request, 'detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)
        if name and description and price and category_id and category:
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                category=category
            )
            return redirect('product_list')
    return render(request, 'product-create.html')


def product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.delete()
    return redirect('product_list')