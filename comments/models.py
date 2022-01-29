from django.db import models
from accounts.models import Account
from products.models import Products


class Comment(models.Model):
    """
    comment model
    """
    product                 = models.ForeignKey(Products, on_delete=models.CASCADE)
    user                    = models.ForeignKey(Account, on_delete=models.CASCADE)
    text                    = models.TextField()
    is_accept               = models.BooleanField(default=False)
    time                    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
