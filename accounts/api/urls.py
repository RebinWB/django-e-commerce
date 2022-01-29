from django.urls import path
from accounts.api.views import user_registration, get_user_info, update_user_info
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", user_registration, name="register_user"),
    path("login/", obtain_auth_token, name="login_user"),
    path("get_user_info/", get_user_info, name="get_user_info"),
    path("update_user_info/", update_user_info, name="update_user_info"),
]

