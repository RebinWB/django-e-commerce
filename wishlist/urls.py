from django.contrib.auth.decorators import login_required
from django.urls import path
from wishlist.views import add_wishlist, ShowAllWishlist, remove_product_from_wishlist

urlpatterns = [
    path("wishlist/", login_required(ShowAllWishlist.as_view()), name="wishlist"),
    path("add-to-wishlist/", add_wishlist, name="add_wishlist"),
    path("wishlist/remove/<pk>/", remove_product_from_wishlist, name="remove_wishlist"),
]

