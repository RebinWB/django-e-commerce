from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from accounts.models import Account
from .forms import CouponForm
from .models import Coupon
from orders.models import Order

@login_required(login_url="login")
def coupon_code_validator(request):
    user_id = request.user.id
    user = Account.objects.get(id=user_id)

    if user is not None:
        user_order = Order.objects.get(is_paid=False, user_id=user.id)
        coupon_form = CouponForm(request.POST or None)
        redirect_path = request.POST.get("next")
        now = datetime.now()

        if coupon_form.is_valid():
            coupon_code = coupon_form.cleaned_data.get("code")

            if user_order.is_used_coupon is False:
                try:
                    coupon = Coupon.objects.get(
                        coupon_code__iexact=coupon_code,
                        valid_from__lte=now,
                        valid_until__gte=now,
                        is_expired=False,
                    )
                    discount = coupon.percentage_amount * (user_order.total / 100)
                    finally_total = (user_order.total - discount)
                    user_order.finally_total = finally_total
                    user_order.discount = discount
                    user_order.is_used_coupon = True
                    user_order.save()
                    messages.success(request, "your coupon code applied successfully!", "success")
                except Coupon.DoesNotExist:
                    messages.error(request, "this code is not valid", "danger")
            else:
                messages.error(request, "you used another coupon before!", "danger")

        return redirect(redirect_path)
