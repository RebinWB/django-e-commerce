from django.urls import path
from .views import coupon_code_validator


urlpatterns = [
    path("apply-coupon-code", coupon_code_validator, name="coupon-code")
]
