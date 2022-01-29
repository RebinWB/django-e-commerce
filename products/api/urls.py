from django.urls import path
from products.api.views import (
    GetAllAvailableProducts,
    CreateProduct, UpdateProduct, DeleteProduct, GetAllCategories,
    CreateCategory, UpdateCategory, DeleteCategory, RetrieveAllSubCategories,
    CreateSubCategory, UpdateSubCategory, DeleteSubCategory, RetrieveGallery,
    CreateGallery, UpdateGallery, DeleteGallery,
)

urlpatterns = [
    path("list", GetAllAvailableProducts.as_view(), name="get_all_products"),
    path("create/", CreateProduct.as_view(), name="create_all_products"),
    path("update/<pk>/", UpdateProduct.as_view(), name="update_products"),
    path("delete/<pk>/", DeleteProduct.as_view(), name="delete_products"),

    # categories api urls
    path("category/", GetAllCategories.as_view(), name="get_all_category"),
    path("category/create/", CreateCategory.as_view(), name="create_category"),
    path("category/update/<pk>/", UpdateCategory.as_view(), name="update_category"),
    path("category/delete/<pk>/", DeleteCategory.as_view(), name="delete_category"),

    # sub categories api urls
    path("sub-category/", RetrieveAllSubCategories.as_view(), name="get_all_sub-category"),
    path("sub-category/create/", CreateSubCategory.as_view(), name="create_sub-category"),
    path("sub-category/update/<pk>/", UpdateSubCategory.as_view(), name="update_sub-category"),
    path("sub-category/delete/<pk>/", DeleteSubCategory.as_view(), name="delete_sub-category"),

    # gallery api urls
    path("gallery/", RetrieveGallery.as_view(), name="get_all_product_gallery"),
    path("gallery/create/", CreateGallery.as_view(), name="create_gallery"),
    path("gallery/update/<pk>/", UpdateGallery.as_view(), name="update_gallery"),
    path("gallery/delete/<pk>/", DeleteGallery.as_view(), name="delete_gallery"),
]








