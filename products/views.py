from django.shortcuts import render
from .models import *

def index(request):

      products1 = Product1.objects.all()
      products2 = Product2.objects.all()
      products3 = Product3.objects.all()
      products4 = Product4.objects.all()

      return render(request, 'index.html',{
          'products1': products1,
          'products2': products2,
          'products3': products3,
          'products4': products4
      })

def productview(request, pk):

    products1 = Product1.objects.filter(id=pk).all()


    return render(request, 'product.html',{
        'products1': products1,

    })

def productview2(request, dk):
    products2 = Product2.objects.filter(id=dk).all()

    return render(request, 'product2.html', {
        'products2': products2,

    })

def productview3(request, sk):
    products3 = Product3.objects.filter(id=sk).all()

    return render(request, 'product3.html', {
        'products3': products3,

    })


def productview4(request, lk):
    products4 = Product4.objects.filter(id=lk).all()

    return render(request, 'product4.html', {
        'products4': products4
    })






