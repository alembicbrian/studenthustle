from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect


from .models import Merchant
from apps.product.models import Product

from .forms import ProductForm

# Create your views here.

def become_merchant(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            merchant = Merchant.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'merchant/become_merchant.html', {'form':form}) 
@login_required
def merchant_admin(request):
    merchant = request.user.merchant
    products = merchant.products.all()

    return render(request, 'merchant/merchant_admin.html', {'merchant': merchant, 'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.merchant = request.user.merchant
            product.slug = slugify(product.title)
            product.save()

            return redirect('merchant_admin')
    else:
        form = ProductForm()
    
    return render(request, 'merchant/add_product.html', {'form': form})
