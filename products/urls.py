from django.urls import path
from .views import (manufacturer_list, manufacturer_detail,
                    product_list, product_detail)

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturer/", manufacturer_list, name="manufacturer-list"),
    path("manufacturer/<int:pk>/", manufacturer_detail, name="manufacturer-detail"),
    #path("products/<int:pk>/", ProductDetialView.as_view(), name="product-detail"),
]