from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from orders.models import Order, OrderDetails
from .forms import RegistrationForm, LoginForm, ProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Account


def register_view(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.username}")

    form = RegistrationForm(request.POST)

    if form.is_valid():
        form.save()
        email = form.cleaned_data.get("email").lower()
        password = form.cleaned_data.get("password1")

        user = authenticate(email=email, password=password)
        login(request, user=user)
        return redirect("home")

    context = {
        "register_form": form
    }
    return render(request, "register.html", context)


def login_view(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "login_form": login_form,
    }
    if not request.user.is_authenticated:
        if login_form.is_valid():
            email = login_form.cleaned_data["email"]
            password = login_form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                login_form = LoginForm()
                return redirect("home")
    else:
        return redirect("home")
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def profile_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = Account.objects.get(id=user_id)
        profile_form = ProfileForm(request.POST or None, initial={
            "user": user,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "email": user.email,
        })
        if profile_form.is_valid():
            firstname = profile_form.cleaned_data["firstname"]
            lastname = profile_form.cleaned_data["lastname"]
            email = profile_form.cleaned_data["email"]

            user.firstname = firstname
            user.lastname = lastname
            user.email = email
            user.save()

        paid_orders = Order.objects.filter(user_id=user_id, is_paid=True).all()
        order_details = OrderDetails.objects.filter(user_id=user_id).last()


        context = {
            "profile_form": profile_form,
            "user_info": user,
            "paid_orders": paid_orders.order_by("-id"),
            "order_details": order_details,
        }

        return render(request, "account_details.html", context)
    return redirect("login")
