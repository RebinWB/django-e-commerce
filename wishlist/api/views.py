from .serializers import WishlistSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from wishlist.models import Wishlist
from rest_framework.filters import OrderingFilter


class GetUserWishlist(generics.ListAPIView):
    """
    retrieve current user's wishlist items

    ** Urls
            <domain>/api/wishlist/
            <domain>/api/wishlist/?ordering=<parameter>
    """
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    authentication_classes = [TokenAuthentication]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        """
        get current user's wishlist items
        """
        return Wishlist.objects.get_queryset().filter(user=self.request.user)


class CreateUserWishlist(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = WishlistSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateUserWishlist(generics.UpdateAPIView):
    """
    update current user's wishlist
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = WishlistSerializer
    lookup_field = "pk"

    def get_queryset(self):
        """
        get current user's wishlist items
        """
        return Wishlist.objects.get_queryset().filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class DeleteUserWishlist(generics.DestroyAPIView):
    """
    delete current user's wishlist
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = WishlistSerializer
    lookup_field = "pk"

    def get_queryset(self):
        """
        get current user's wishlist items
        """
        return Wishlist.objects.get_queryset().filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
