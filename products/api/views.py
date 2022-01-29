from django.http import Http404
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import ProductSerializer, CategorySerializer, SubCategorySerializer, GallerySerializer
from products.models import Products, Category, SubCategory, Gallery
from rest_framework.filters import SearchFilter, OrderingFilter


class GetAllAvailableProducts(generics.ListAPIView):
    """
    retrieve all available products

    ** Urls:
            <domain>/api/products/list
            <domain>/api/products/list?search=men
            <domain>/api/products/list?ordering=<parameter>
            <domain>/api/products/list?search=men&ordering=<parameter>
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "description"]

    def get_queryset(self):
        return Products.objects.filter(is_available=True).all()


class CreateProduct(generics.CreateAPIView):
    """
    create new product
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()


class UpdateProduct(generics.UpdateAPIView):
    """
    get pk from URL and update product
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()


class DeleteProduct(generics.DestroyAPIView):
    """
    get product pk from URL and delete it
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        instance.delete()


# ----------- Category APIs Section -----------

class GetAllCategories(generics.ListAPIView):
    """
    retrieve all categories

    ** Urls:
            <domain>/api/products/category/
            <domain>/api/products/category/?search=<parameter>
            <domain>/api/products/category/?ordering=<parameter>
            <domain>/api/products/category/?search=<parameter>&ordering=<parameter>
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title"]


class CreateCategory(generics.CreateAPIView):
    """
    create new category
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()


class UpdateCategory(generics.UpdateAPIView):
    """
    update category
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()


class DeleteCategory(generics.DestroyAPIView):
    """
    delete category
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"


# ----------- SubCategory APIs Section -----------

class RetrieveAllSubCategories(generics.ListAPIView):
    """
    retrieve all sub categories

    ** Urls:
            <domain>/api/products/sub-category/
            <domain>/api/products/sub-category/?search=<parameter>
            <domain>/api/products/sub-category/?ordering=<parameter>
            <domain>/api/products/sub-category/?search=<parameter>&ordering=<parameter>
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title"]


class CreateSubCategory(generics.CreateAPIView):
    """
    create new sub category
    """
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save()


class UpdateSubCategory(generics.UpdateAPIView):
    """
    update sub category
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()


class DeleteSubCategory(generics.DestroyAPIView):
    """
    delete sub category
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        instance.delete()


# ----------- Gallery APIs Section -----------

class RetrieveGallery(generics.ListAPIView):
    """
    retrieve all Gallery Pics for specific product
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = GallerySerializer

    def get_queryset(self):
        """
        receive product id from body and get it's all gallery pics
        """
        return Gallery.objects.get_queryset().filter(
            product_id=self.request.POST.get("product_id")).all()


class CreateGallery(generics.CreateAPIView):
    """
    create new pic in specific product gallery
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = GallerySerializer

    def perform_create(self, serializer):
        serializer.save()


class UpdateGallery(generics.UpdateAPIView):
    """
    update gallery
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()


class DeleteGallery(generics.DestroyAPIView):
    """
    delete gallery pic
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        instance.delete()


