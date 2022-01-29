import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from accounts.models import Account
from coupon.forms import CouponForm
from orders.forms import OrderForm, OrderDetailsForm
from orders.models import Order, Cart, OrderDetails
from products.models import Products
from django.http import Http404, HttpResponse
import requests
import json



@login_required(login_url="login")
def add_to_cart(request):
    """
    add product in order

    add to it if there is an unpaid order. Otherwise create one 
    """
    if request.user.is_authenticated:
        order_form = OrderForm(request.POST or None)
        if order_form.is_valid():
            try:
                order = Order.objects.get(user_id=request.user.id, is_paid=False)
            except:
                order = Order.objects.create(user_id=request.user.id, is_paid=False)
                order.save()
            product_id = order_form.cleaned_data["product_id"]
            quantity = order_form.cleaned_data["quantity"]
            size_title = request.POST.get("size_form")
            # print(size_title)

            product = Products.objects.get(id=product_id)
            size = product.size.get(title=size_title)
            total = quantity * product.price
            try:
                cart = order.cart_set.get(product=product, size=size)
                cart.quantity += quantity
                cart.total = cart.total + total
                cart.save()
                return redirect("open_order")
            except:
                cart = order.cart_set.create(product=product, quantity=quantity, total=total, size=size)
                cart.save()
                return redirect("open_order")

    return redirect("login")


@login_required(login_url="login")
def cart_products_list(request):
    """
    list of all carts in unpaid order
    """
    context = {
        "order": None,
        "cart": None,
        "total-price": 0
    }

    try:
        open_order = Order.objects.get(user_id=request.user.id, is_paid=False)
    except Order.DoesNotExist:
        open_order = Order.objects.create(user_id=request.user.id, is_paid=False)

    if open_order is not None:
        total = open_order.cart_set.aggregate(Sum('total'))
        open_order.total = total["total__sum"]
        open_order.save()
        coupon_form = CouponForm(request.POST or None)
        # print(open_order.total)
        context["order"] = open_order
        context["cart"] = Cart.objects.filter(order_id=open_order.id).all()
        context["total-price"] = open_order.total
        context["coupon_form"] = coupon_form

    return render(request, "order_template.html", context)


@login_required(login_url="login")
def remove_product(request, *args, **kwargs):
    """
    remove cart from order if exists
    """
    if request.user.is_authenticated:
        cart_id = kwargs["cart_id"]
        user_id = request.user.id
        try:
            order = Order.objects.get(user_id=user_id, is_paid=False)
        except:
            raise Http404("Your Order Not Found")

        cart = order.cart_set.get(id=cart_id)
        if cart is not None:
            cart.delete()
        return redirect("open_order")

@login_required(login_url="login")
def add_cart_quantity(request, *args, **kwargs):
    """
    add a item in the cart quntity
    """
    user = request.user
    if user is not None:
        try:
            open_order = Order.objects.get(user=user, is_paid=False)
        except Order.DoesNotExist:
            raise Http404

        cart_id = kwargs["cart_id"]
        try:
            cart = open_order.cart_set.get(id=cart_id)
            cart.quantity += 1 
            cart.total = cart.total + cart.product.price
            cart.save()
        except Cart.DoesNotExist:
            raise Http404

    return redirect("open_order")


@login_required(login_url="login")
def decrease_cart_quantity(request, *args, **kwargs):
    """
    delete one item from cart
    """
    user = request.user
    if user is not None:
        try:
            open_order = Order.objects.get(user=user, is_paid=False)
        except Order.DoesNotExist:
            raise Http404

        cart_id = kwargs["cart_id"]
        try:
            cart = open_order.cart_set.get(id=cart_id)
            cart.quantity -= 1 
            cart.total = cart.total - cart.product.price
            cart.save()
        except Cart.DoesNotExist:
            raise Http404

        if cart.quantity <= 0:  # delete cart if it quantity smaller than 1 item
            cart.delete()

    return redirect("open_order")

@login_required(login_url="login")
def order_delivery_details_view(request):
    """
    order delivery information view

    if any information exists about user's delivery, initial form with those
    """
    if request.user.is_authenticated:
        user_id = request.user.id
        user = Account.objects.get(id=user_id)
        coupon_form = CouponForm(request.POST or None)
        try:
            order_checkout = OrderDetails.objects.filter(user=user).last()
            order_details_form = OrderDetailsForm(request.POST or None, initial={
                "email": user.email,
                "first_name": user.firstname,
                "last_name": user.lastname,
                "phone": order_checkout.phone,
                "province": order_checkout.province,
                "city": order_checkout.city,
                "address": order_checkout.address,
                "company_name": order_checkout.company_name,
                "postcode": order_checkout.postcode,
            })
        except:
            order_details_form = OrderDetailsForm(request.POST or None, initial={
                "email": user.email,
                "first_name": user.firstname,
                "last_name": user.lastname,
            })

        if order_details_form.is_valid():
            phone = order_details_form.cleaned_data["phone"]
            province = order_details_form.cleaned_data["province"]
            city = order_details_form.cleaned_data["city"]
            address = order_details_form.cleaned_data["address"]
            company_name = order_details_form.cleaned_data["company_name"]
            postcode = order_details_form.cleaned_data["postcode"]

            try:
                order_details = OrderDetails.objects.filter(user=user, phone=phone).last()
                order_details.province = province
                order_details.city = city
                order_details.address = address
                order_details.company_name = company_name
                order_details.postcode = postcode
            except:
                order_details = OrderDetails.objects.create(
                    user=user,
                    phone=phone,
                    province=province,
                    city=city,
                    address=address,
                    company_name=company_name,
                    postcode=postcode,
                )

            order_details.save()
            return redirect("checkout")

        context = {
            "order_details_form": order_details_form,
            "coupon_form": coupon_form
        }
        return render(request, "order_details.html", context)

    return redirect("login")


@login_required(login_url="login")
def checkout(request):
    """
    checkout view
    """
    if request.user.is_authenticated:
        user_id = request.user.id
        user = Account.objects.get(id=user_id)
        context = {}
        if user is not None:
            open_order = Order.objects.get(is_paid=False, user_id=user.id)
            open_order_products = open_order.cart_set.all()
            if open_order_products.count() > 0:
                context["open_order"] = open_order
                context["open_order_products"] = open_order_products
                return render(request, "checkout.html", context)
            else:
                raise Http404("You Haven't Any Unpaid Order")
        raise Http404
    return redirect("login")



MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'

@login_required(login_url="login")
def send_request(request):
    user = Account.objects.get(id=request.user.id)
    open_order = Order.objects.get(is_paid=False, user_id=user.id)
    if open_order.finally_total:
        amount = open_order.finally_total
    else:
        amount = open_order.total

    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request, *args, **kwargs):
    order_id = kwargs.get("order_id")
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                user_order = Order.objects.get(id=order_id, user_id=request.user.id)
                user_order.is_paid = True
                user_order.payment_date = datetime.datetime.now()
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')

