from django.contrib import admin
from coupon.models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = [
        "coupon_code",
        "percentage_amount",
        "valid_from",
        "valid_until",
        "is_expired",
    ]
    list_filter = [
        "is_expired",
    ]
    list_editable = [
        "is_expired",
    ]
