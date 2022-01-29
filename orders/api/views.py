from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from orders.api.serializers import OrderSerializer, CartSerializer, OrderDetailSerializer
from orders.models import Order, Cart, OrderDetails


class GetUnpaidUserOrder(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        """
        get user order that is_paid = False
        """
        queryset = Order.objects.get(user=request.user, is_paid=False)
        serializer = OrderSerializer(queryset, many=False)
        return Response(serializer.data)


class GetPaidUserOrder(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        """
        get user order that is_paid = True
        """
        queryset = Order.objects.filter(user=request.user, is_paid=True)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class GetAllOrders(generics.ListAPIView):
    """
    get all orders [ALLOWED FOR ADMINS ONLY]
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateUserOrder(generics.CreateAPIView):
    """
    create user order
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        """
        look for user order. if not exist, create new one. else raise an error
        """
        try:
            Order.objects.get(user=self.request.user, is_paid=False)
            raise ValidationError
        except Order.DoesNotExist:
            serializer.save(user=self.request.user)


class UpdateUserOrder(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_object(self, user):
        """
        try to get user order that owned by current user
        """
        try:
            queryset = Order.objects.get(user=user, is_paid=False)
            return queryset
        except Order.DoesNotExist:
            raise Http404

    def put(self, request):
        """
        edit user order with sent parameters
        """
        queryset = self.get_object(user=self.request.user)
        serializer = OrderSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserOrder(generics.DestroyAPIView):
    """
    delete user order that it's pk received from url
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "pk"


# ----------- Carts APIs Section -----------

class GetAllUserCarts(generics.ListAPIView):
    """
    get all user's carts that's in unpaid orders
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(order__user=self.request.user, order__is_paid=False)


class CreateUserCart(generics.CreateAPIView):
    """
    create cart for user. if unpaid order is exist append cart into
    this one, else create new order instance
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        """
        try to find unpaid order or create new one
        """
        try:
            order = Order.objects.get(user=self.request.user, is_paid=False)
            serializer.save(order=order)
        except Order.DoesNotExist:
            order = Order.objects.create(user=self.request.user, is_paid=False)
            serializer.save(order=order)


class UpdateUserCart(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk, user):
        """
        try to get unpaid cart that it's pk equals to received pk
        """
        try:
            return Cart.objects.get(pk=pk, order__is_paid=False, order__user=user)
        except Cart.DoesNotExist:
            raise Http404

    def put(self, request):
        """
        update selected cart
        """
        queryset = self.get_object(pk=self.request.POST.get("pk"), user=self.request.user)
        serializer = CartSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserCart(generics.DestroyAPIView):
    """
    delete user cart that it's pk received from url
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CartSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Cart.objects.filter(order__user=self.request.user, order__is_paid=False)


# ----------- Carts APIs Section -----------

class GetAllOrderDetails(generics.ListAPIView):
    """
    retrieve all users Order Delivery Details
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderDetailSerializer
    queryset = OrderDetails.objects.all()


class GetUserOrderDetails(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, user):
        """
        try to get first order delivery details by user
        """
        try:
            return OrderDetails.objects.get_queryset().filter(user=user).first()
        except OrderDetails.DoesNotExist:
            raise Http404

    def get(self, request):
        """
        if order delivery is not None return it. else return
        a response with http404 status (Not Found)
        """
        queryset = self.get_object(user=self.request.user)
        if queryset is not None:
            serializer = OrderDetailSerializer(queryset)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class CreateUserOrderDelivery(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        """
        create new user order delivery details
        """
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserOrderDetails(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, user, pk):
        """
        try to get requested order delivery details or raise http404 error (Not Found)
        """
        try:
            return OrderDetails.objects.get(user=user, pk=pk)
        except OrderDetails.DoesNotExist:
            raise Http404


    def put(self, request):
        """
        update received order delivery details
        """
        queryset = self.get_object(user=self.request.user, pk=self.request.POST.get("pk"))
        serializer = OrderDetailSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserOrderDeliveryDetails(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        """
        try to get order delivery details by pk or raise http404 error (Not Found)
        """
        try:
            return OrderDetails.objects.get(pk=pk)
        except OrderDetails.DoesNotExist:
            raise Http404

    def delete(self, request):
        """
        finish him :)
        """
        queryset = self.get_object(
            pk=self.request.POST.get("pk"),
        )
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





