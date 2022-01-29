from django.urls import path
from orders.api.views import (
    GetUnpaidUserOrder,
    GetAllOrders,
    CreateUserOrder,
    UpdateUserOrder,
    DeleteUserOrder,
    GetPaidUserOrder,
    GetAllUserCarts,
    CreateUserCart,
    UpdateUserCart,
    DeleteUserCart,
    GetUserOrderDetails,
    CreateUserOrderDelivery,
    UpdateUserOrderDetails,
    DeleteUserOrderDeliveryDetails,
    GetAllOrderDetails,
)


urlpatterns = [
    path("get_unpaid_order/", GetUnpaidUserOrder.as_view(), name="get_unpaid_order"),
    path("get_paid_order/", GetPaidUserOrder.as_view(), name="get_paid_order"),
    path("get_all/", GetAllOrders.as_view(), name="get_all_orders"),
    path("create/", CreateUserOrder.as_view(), name="create_order"),
    path("update/", UpdateUserOrder.as_view(), name="update_order"),
    path("delete/<pk>", DeleteUserOrder.as_view(), name="delete_order"),


    # cart urls
    path("carts/get/", GetAllUserCarts.as_view(), name="get_all_carts"),
    path("carts/create/", CreateUserCart.as_view(), name="create_cart"),
    path("carts/update/", UpdateUserCart.as_view(), name="update_cart"),
    path("carts/delete/<pk>", DeleteUserCart.as_view(), name="delete_cart"),


    # order delivery details urls
    path("delivery/", GetAllOrderDetails.as_view(), name="get_all_user_order_delivery"),
    path("delivery/get/", GetUserOrderDetails.as_view(), name="get_user_order_delivery"),
    path("delivery/create/", CreateUserOrderDelivery.as_view(), name="post_user_order_delivery"),
    path("delivery/update/", UpdateUserOrderDetails.as_view(), name="update_user_order_delivery"),
    path("delivery/delete/", DeleteUserOrderDeliveryDetails.as_view(), name="delete_user_order_delivery"),
]




