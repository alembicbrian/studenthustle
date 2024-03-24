from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Merchant

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

    return render(request, 'merchant/merchant_admin.html', {'merchant': merchant})

    