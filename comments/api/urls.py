from django.urls import path
from .views import GetCommentsList, UpdateComments, CreateComments, DeleteComment

urlpatterns = [
    path("create/", CreateComments.as_view(), name="create_comment"),
    path("get/", GetCommentsList.as_view(), name="get_product_comments"),
    path("update/<pk>", UpdateComments.as_view(), name="update_comment"),
    path("delete/<pk>", DeleteComment.as_view(), name="delete_comment"),
]






