from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Please Enter Email")
        if not username:
            raise ValueError("Please Enter Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

# User Profile Picture Handler
def default_profile_image():
    return f"defaults/default.png"

def user_profile_uploader(instance, filename):
    filename = f"Profile_Image.jpg"
    return f"accounts/{instance.username}-{instance.id}/{filename}"


# Main Account Model
class Account(AbstractBaseUser):
    email                   = models.EmailField(max_length=120, unique=True)
    username                = models.CharField(max_length=60, unique=True)
    firstname               = models.CharField(max_length=60, blank=True)
    lastname                = models.CharField(max_length=60, blank=True)
    date_joined             = models.DateTimeField(auto_now_add=True)
    last_login              = models.DateTimeField(auto_now=True)
    is_active               = models.BooleanField(default=True)
    is_admin                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    profile_image           = models.ImageField(max_length=255, upload_to=user_profile_uploader, blank=True, null=True, default=default_profile_image)
    USERNAME_FIELD          = "email"
    REQUIRED_FIELDS         = ["username"]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username

    objects = AccountManager()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    create a Unique Token for each user when created = True
    """

    if created:
        Token.objects.create(user=instance)
        for user in Account.objects.all():
            Token.objects.get_or_create(user=user)