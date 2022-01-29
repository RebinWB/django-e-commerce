from django.urls import path
from wishlist.api.views import (
    GetUserWishlist,
    CreateUserWishlist,
    UpdateUserWishlist, DeleteUserWishlist,
)

urlpatterns = [
    path("", GetUserWishlist.as_view(), name="get_user_wishlist"),
    path("create/", CreateUserWishlist.as_view(), name="create_user_wishlist"),
    path("update/<pk>/", UpdateUserWishlist.as_view(), name="update_user_wishlist"),
    path("delete/<pk>/", DeleteUserWishlist.as_view(), name="delete_user_wishlist"),
]

