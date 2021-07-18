from django.shortcuts import render

from .models import Product


def home(request):
    products = Product.objects.filter(is_active=True)

    # shu yerda updated_at modeldagi
    latest_products = Product.objects.filter(is_active=True).order_by("-updated_at")[:6]
    #  narxi boyicha kamayish tartibida 

    # latest_products = Product.objects.filter(is_active=True).order_by("title")[:6]
    #  nomi boyicha osish tartibida

    context = {
        "products": products,
        "latest_products": latest_products
    }
    return render(request, "index.html", context)