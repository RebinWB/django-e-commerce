from django.urls import path

from comments.views import product_comment

urlpatterns = [
    path("get-comment", product_comment, name="comment")
]

