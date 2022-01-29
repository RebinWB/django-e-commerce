from django.urls import path
from products.views import (
    ProductsList,
    product_details,
    return_category_objects,
    return_subcategory_objects,
    SearchProducts,
)

urlpatterns = [
    path("products/", ProductsList.as_view(), name="products"),
    path("products/<int:product_id>/<slug:slug>/", product_details, name="product_details"),
    path("products/<str:category>/", return_category_objects, name="categories"),
    path("products/<str:category>/<str:sub_category>/", return_subcategory_objects, name="sub_categories"),
    path("products/search", SearchProducts.as_view(), name="search"),
]
