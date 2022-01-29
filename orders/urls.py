from django.urls import path
from orders.views import cart_products_list, add_to_cart, remove_product, order_delivery_details_view, checkout, \
    send_request, verify

urlpatterns = [
    path("cart/", cart_products_list, name="open_order"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("remove/<cart_id>/", remove_product, name="remove_item"),
    path("cart/order_details/", order_delivery_details_view, name="order_detail"),
    path("cart/order_details/checkout/", checkout, name="checkout"),
    path('cart/order_details/checkout/request/', send_request, name='request'),
    path('verify/<order_id>/', verify, name='verify'),
]


