from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from products.models import Product


def home(request):
    return render(request, 'index.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'detail.html', {'category': category, 'products': products})


def category_create(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')
        Category.objects.create(category_name=category_name, description=description)
        return redirect('category_list')
    return render(request, 'create-category.html')
