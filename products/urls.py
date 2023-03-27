from django.urls import path

from products.views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', productview, name='product'),
    path('product2/<int:dk>/', productview2, name='product2'),
    path('product3/<int:sk>/', productview3, name='product3'),
    path('product4/<int:lk>/', productview4, name='product4'),
    path('producttop/<int:id>/', producttopview, name="producttop"),
    path('products/', products, name='products'),
    path('productbottom/', productbottom, name='productbottom')
]