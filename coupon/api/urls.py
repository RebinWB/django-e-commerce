from django.urls import path
from .views import (
    GetAllCoupons,
    CreateCoupon,
    UpdateCoupons,
    DeleteCoupons,
)

urlpatterns = [
    path("get/", GetAllCoupons.as_view(), name="get_coupon"),
    path("create/", CreateCoupon.as_view(), name="create_coupon"),
    path("update/<pk>", UpdateCoupons.as_view(), name="update_coupon"),
    path("delete/<pk>", DeleteCoupons.as_view(), name="delete_coupon"),
]

