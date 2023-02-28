from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Product
from webapp.models import StatusChoices
from webapp.forms import ProductsListForm


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product, "choices": StatusChoices.choices})


def add_view(request):
    if request.method == "GET":
        form = ProductsListForm()
        return render(request, "product_add.html", context={'form': form})
    elif request.method == "POST":
        form = ProductsListForm(request.POST)
        if form.is_valid():
            product_data = {
                'title': request.POST.get('title'),
                'description': request.POST.get('description'),
                'image': request.POST.get('image'),
                'category': request.POST.get('category'),
                'rest': request.POST.get('rest'),
                'price': request.POST.get('price')
            }
            product = Product.objects.create(**product_data)
            return redirect('product_detail', pk=product.pk)


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductsListForm(initial={
            'title': product.title,
            'description': product.description,
            'image': product.image,
            'category': product.category,
            'rest': product.rest,
            'price': product.price
        })
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        product.title = request.POST.get('title')
        product.description = request.POST.get('description')
        product.image = request.POST.get('image')
        product.category = request.POST.get('category')
        product.rest = request.POST.get('rest')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'product_update.html', context={'product': product})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')
