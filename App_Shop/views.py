from django.shortcuts import render


from django.views.generic import ListView, DetailView

from App_Shop.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(ListView):
    #the ListView is by default providing the object_list
    model =Product
    template_name='App_Shop/home.html'

class ProductDetail(DetailView, LoginRequiredMixin ):
    #writing  the loginRequiredMixin at the beginning those not allow u to access the product details if you're not login
    model = Product
    template_name= 'App_Shop/product_detail.html'
