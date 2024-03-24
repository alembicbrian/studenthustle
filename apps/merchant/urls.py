from django.contrib.auth import views as auth_views
from django.urls import path

from .import views

urlpatterns  = [
    path('become_merchant/', views.become_merchant, name='become_merchant'),
    path('merchant_admin/', views.merchant_admin, name='merchant_admin'),
    path('add-product/', views.add_product, name='add_product'),


    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='merchant/login.html'), name='login'),
]