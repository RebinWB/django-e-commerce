from django.urls import path
from contact.views import contact_view

urlpatterns = [
    path("contact/", contact_view, name="contact")
]
