from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CommentSerializer
from ..models import Comment


class CreateComments(generics.CreateAPIView):
    """
    create comments for products [ALLOWED FOR ALL AUTHENTICATED USERS]
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class GetCommentsList(generics.ListAPIView):
    """
    get all comments of a specific product
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(product_id=self.request.GET.get("product_id"))


class UpdateComments(generics.RetrieveUpdateAPIView):
    """
    edit all fields of comments [ONLY ALLOWED FOR ADMINS]
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DeleteComment(generics.DestroyAPIView):
    """
    delete specific comment (By PK)
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Comment.objects.all()
    lookup_field = 'pk'



