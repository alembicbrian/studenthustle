from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Merchant

# Create your views here.

def become_merchant(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()
    
    return render(request, 'merchant/become_merchant.html')

    