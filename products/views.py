from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def products_view(request):
    products = Product.objects.using('products_db').all()
    return render(request, 'products/products.html', {'products': products})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {
        'form': form
    })