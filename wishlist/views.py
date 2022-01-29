from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import ListView
from accounts.models import Account
from products.models import Products
from wishlist.forms import WishlistForm
from wishlist.models import Wishlist


@login_required(login_url="login")
def add_wishlist(request):
    user_id = request.user.id
    user = Account.objects.get(id=user_id)
    wishlist_form = WishlistForm(request.POST or None)

    if wishlist_form.is_valid():
        product_id = wishlist_form.cleaned_data.get("product_id")

        err_url = request.POST.get("next")
        product = Products.objects.get(id=product_id)
        try:
            Wishlist.objects.get(product=product, user_id=user_id)
            messages.error(request, "this product added to your wishlist before")
            return redirect(err_url)
        except Wishlist.DoesNotExist:
            wishlist = Wishlist.objects.create(product=product, user=user)
            wishlist.save()

        return redirect("wishlist")


class ShowAllWishlist(ListView):

    template_name = "wishlist.html"
    model = Wishlist
    queryset = Wishlist.objects.all()

    def get_queryset(self):
        query = Wishlist.objects.get_queryset().filter(user_id=self.request.user.id).all()
        print(query)
        return query


@login_required(login_url="login")
def remove_product_from_wishlist(request, *args, **kwargs):
    wishlist_id = kwargs["pk"]
    user_id = request.user.id
    user = Account.objects.get(id=user_id)
    if user is not None:
        try:
            wishlist = Wishlist.objects.get(user=user, id=wishlist_id)
            wishlist.delete()
        except Wishlist.DoesNotExist:
            raise Http404

    return redirect("wishlist")
