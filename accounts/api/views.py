from accounts.models import Account
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import AccountSerializer, UserInformation
from rest_framework.authtoken.models import Token


USERNAME = "username"
EMAIL = "email"
TOKEN = "token"
RESPONSE = "response"


@api_view(["POST"])
def user_registration(request):
    """
    register user using restful api [Django Rest Framework]
    """

    serializer = AccountSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        data[RESPONSE] = "Registration Success"
        data[USERNAME] = user.username
        data[EMAIL] = user.email
        data[TOKEN] = Token.objects.get(user=user).key
    else:
        data[RESPONSE] = serializer.errors

    return Response(data)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_user_info(request):
    """
    show user information [(email, username) ONLY]
    """

    try:
        user = Account.objects.get(id=request.user.id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserInformation(user)
    return Response(serializer.data, status=status.HTTP_200_OK)




@permission_classes([IsAuthenticated])
@api_view(["PUT"])
def update_user_info(request):
    """
    edit user information [(username, email) ONLY]
    """

    try:
        user = Account.objects.get(id=request.user.id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserInformation(user, data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data[RESPONSE] = "User Information Edited Successfully"
        data[EMAIL] = account.email
        data[USERNAME] = account.username
    else:
        data[RESPONSE] = serializer.errors

    return Response(data)



