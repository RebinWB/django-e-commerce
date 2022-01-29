from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ContactSerializer
from contact.models import Contact


class CreateContact(generics.CreateAPIView):
    """
    create new contact-us form
    """
    serializer_class = ContactSerializer


class GetAllContacts(generics.ListAPIView):
    """
    get all contact-us forms
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]


class DeleteContact(generics.DestroyAPIView):
    """
    delete specific contact-us forms
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'pk'

