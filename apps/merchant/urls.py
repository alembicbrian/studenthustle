from django.urls import path
from .import views

urlpatterns  = [
    path('become_merchant/', views.become_merchant, name='become_merchant')
]