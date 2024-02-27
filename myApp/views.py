from django.shortcuts import render, redirect
from .models import *

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', { 'products' : products })

def product_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        discount = request.POST.get('discount')

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            category = None
        
        if category:
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                category=category,
                discount=discount,
            )
            return redirect('product_list')
    categories = Category.objects.all()
    return render(request, 'product_add.html', {'categories': categories})

def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        product = None
    
    if request.method == "POST" and product:
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        discount = request.POST.get('discount')
    
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            category = None
        
        if category:
           product.name = name
           product.description = description
           product.price = price
           product.category = category
           product.discount = discount
           product.save()
           return redirect('product_list')
        
    categories = Category.objects.all()
    return render(request, 'product_update.html', {'product': product, 'categories': categories})
                    

def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        product = None
    return render(request, 'product_details.html', {'product': product})

def product_delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        product = None
    
    if request.method == "POST" and product:
        product.delete()
        return redirect('product_list')
    
    return render(request, 'product_delete.html', {'product': product})
