from django.urls import path
from .views import about_configuration

urlpatterns = [
    path("about/", about_configuration, name="about")
]


