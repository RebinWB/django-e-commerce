from django.contrib import admin
from orders.models import Cart, Order, OrderDetails


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "total",
        "is_paid",
        "payment_date",
        "finally_total",
    ]

    list_filter = [
        "is_paid",
    ]

    search_fields = [
        "user",
    ]

    list_editable = [
        "is_paid",
    ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = [
        "order",
        "product",
        "quantity",
        "total",

    ]

@admin.register(OrderDetails)
class OrderCheckout(admin.ModelAdmin):

    list_display = [
        "user",
        "phone",
        "postcode",
        "province",
        "city",
    ]

