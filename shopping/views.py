from django.shortcuts import render

# Create your views here.

def shopping_admin(request):
    return render(request, "shopping/index.html")

def shopping_shop(request):
    return render(request, "shopping/index-shop.html")

def shopping_item(request):
    return render(request, "shopping/index-item.html")
