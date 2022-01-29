from django.shortcuts import render
from rest_framework.authtoken.models import Token

from accounts.models import Account
from products.models import Category, Products
from settings.models import Slider, Banner, WebSiteDetails


def home_page(request):
    slider = Slider.objects.get_queryset().order_by("-id")[:3]
    mini_banner = Banner.objects.get_queryset().filter(banner_type="Mini").order_by("-id")[:3]
    large_banner = Banner.objects.get_queryset().filter(banner_type="Large").order_by("-id")[:1]
    latest_products = Products.objects.get_queryset().order_by("-id")[:10]
    for user in Account.objects.all():
        Token.objects.get_or_create(user=user)
    recently_viewed = None
    if "recently_viewed" in request.session:

        products_in_session = request.session["recently_viewed"]
        # print(products_in_session)
        if products_in_session is not None:
            recently_viewed = Products.objects.filter(id__in=products_in_session).distinct()
    # print(recently_viewed)

    context = {
        "latest_products": latest_products,
        "slider": slider,
        "mini_banner": mini_banner,
        "large_banner": large_banner,
        "recently_viewed": recently_viewed,
    }
    return render(request, "homePage.html", context)


def header_partial_view(request):
    categories = Category.objects.all()[:4]
    context = {
        "categories": categories
    }
    return render(request, 'components/header.html', context)

