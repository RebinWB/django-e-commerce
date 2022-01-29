from django.urls import path
from contact.api.views import CreateContact, GetAllContacts, DeleteContact

urlpatterns = [
    path("create/", CreateContact.as_view(), name="create_contact"),
    path("get/", GetAllContacts.as_view(), name="get_contacts"),
    path("delete/<pk>", DeleteContact.as_view(), name="delete_contact"),
]



