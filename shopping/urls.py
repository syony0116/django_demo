from django.urls import path

from shopping import views

urlpatterns = [
    path("admin/", views.shopping_admin),
    path("shop/", views.shopping_shop),
    path("item/", views.shopping_item)
]
