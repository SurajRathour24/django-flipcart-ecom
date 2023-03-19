import queue
from unicodedata import category
from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from django.db.models import F

# Create your views here.
def home(request):
    elec = Product.objects.filter(category="electronics")
    print (elec.query)

    topFashionDeals = Product.objects.filter(category='fashion').order_by('?')

    bestBrands = Product.objects.filter( discounted_price__gte = 1200).filter(category='fashion')
    topOffers =  Product.objects.filter(discounted_price__gte = 3000)
    print(topOffers)
    context = {
        'elec' : elec,
        'topFashionDeals' : topFashionDeals,
        'bestBrands' : bestBrands,
        'topOffers' : topOffers,
    }

    return render(request, 'core/index.html', context)


def cart(request):
    if request.user.is_authenticated:
        return render(request, 'core/cart.html')
    else:
        return HttpResponseRedirect('/account/signin')


def singleProduct(request, id):
    productData = Product.objects.get(pk=id)
    
    context = {
        'pd' : productData
    }



    return render(request, 'core/single-product.html', context)