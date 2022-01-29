from django.http import Http404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CouponSerializer
from coupon.models import Coupon


class GetAllCoupons(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        """
        get all coupons before creating new one
        """
        queryset = Coupon.objects.all()
        serializer = CouponSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCoupon(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        """
        create new coupon
        """
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCoupons(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        """
        try to get coupon by id
        """
        try:
            return Coupon.objects.get(pk=pk)
        except Coupon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        """
        edit specific coupon [get it by pk]
        """
        queryset = self.get_object(pk=pk)
        serializer = CouponSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCoupons(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        """
        try to get coupon by id
        """
        try:
            return Coupon.objects.get(pk=pk)
        except Coupon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """
        delete coupon code
        """
        queryset = self.get_object(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




