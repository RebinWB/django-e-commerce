from django.db import models
from accounts.models import Account
from products.models import Products, Size


STATUS = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Delivered", "Delivered"),
)


class Order(models.Model):
    """
    Order model. all order instances have a status. [default = 'pending']
    """
    user                    = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_paid                 = models.BooleanField(default=False)
    payment_date            = models.DateTimeField(blank=True, null=True)
    delivery_status         = models.CharField(max_length=150, choices=STATUS, default="Pending")
    total                   = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_used_coupon          = models.BooleanField(default=False)
    discount                = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    finally_total           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    """
    cart model
    each item in order is a cart instance
    """
    order                   = models.ForeignKey(Order, on_delete=models.CASCADE)
    product                 = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity                = models.IntegerField()
    total                   = models.DecimalField(max_digits=7, decimal_places=2)
    size                    = models.ForeignKey(Size, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.product.name


class OrderDetails(models.Model):
    """
    order delivery details model
    """
    user                    = models.ForeignKey(Account, on_delete=models.CASCADE)
    phone                   = models.CharField(max_length=15)
    province                = models.CharField(max_length=150)
    city                    = models.CharField(max_length=150)
    address                 = models.TextField()
    company_name            = models.CharField(max_length=150, blank=True, null=True)
    postcode                = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username + " Checkout"

    class Meta:
        ordering = ["-id"]  # order by last to first
        verbose_name_plural = "Order Details"

