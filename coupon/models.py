from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=60, unique=True)
    percentage_amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.coupon_code

