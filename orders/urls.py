from django.urls import path
from orders.views import (
    cart_products_list,
    add_to_cart,
    remove_product,
    order_delivery_details_view,
    checkout,
    send_request,
    verify, 
    add_cart_quantity,
    decrease_cart_quantity,
    )

urlpatterns = [
    path("cart/", cart_products_list, name="open_order"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("increase_quantity/<cart_id>/", add_cart_quantity, name="increase_quantity"),
    path("decrease_quantity/<cart_id>/", decrease_cart_quantity, name="decrease_quantity"),
    path("remove/<cart_id>/", remove_product, name="remove_item"),
    path("cart/order_details/", order_delivery_details_view, name="order_detail"),
    path("cart/order_details/checkout/", checkout, name="checkout"),
    path('cart/order_details/checkout/request/', send_request, name='request'),
    path('verify/<order_id>/', verify, name='verify'),
]


