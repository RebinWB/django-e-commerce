from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView
from orders.forms import OrderForm
from comments.forms import CommentForm
from comments.models import Comment
from wishlist.forms import WishlistForm
from .models import Products, SubCategory, Category


# Class Based View for Product List
class ProductsList(ListView):
    template_name = "productsList.html"
    paginate_by = 12

    def get_queryset(self):
        return Products.objects.filter(is_available=True)


def product_details(request, *args, **kwargs):
    product_id = kwargs["product_id"]

    # session for recently products that viewed by user
    if "recently_viewed" in request.session:
        if product_id in request.session["recently_viewed"]:
            request.session["recently_viewed"].remove(product_id)
        request.session["recently_viewed"].insert(0, product_id)
    else:
        request.session["recently_viewed"] = [product_id]

    request.session.modified = True
    request.session.set_expiry(0)

    # this product
    product = Products.objects.get(id=product_id)

    # comment form
    comment_form = CommentForm(request.POST or None, initial={"product_id": product_id, "user_id": request.user.id})
    
    # add to order form
    order_form = OrderForm(request.POST or None, initial={"product_id": product_id})
    
    # add to wishlist form
    wishlist_form = WishlistForm(request.POST or None, initial={"product_id": product_id})
    
    # all product accepted comments
    comments = Comment.objects.filter(product=product, is_accept=True).all()
    
    # all related products to this product [based on category field]
    related_products = Products.objects.filter(category=product.category).all()

    context = {
        "product": product,
        "order_form": order_form,
        "wishlist_form": wishlist_form,
        "comment_form": comment_form,
        "comments": comments,
        "related_products": related_products,

    }

    return render(request, "productDetails.html", context)


def return_category_objects(request, *args, **kwargs):
    category = kwargs["category"]
    try:
        products = Products.objects.get_product_by_category(category)
        # print(products)
    except Products.DoesNotExist:
        raise Http404("Not Found any Products in this Category!")

    context = {
        "object_list": products
    }

    return render(request, "productsList.html", context)


def return_subcategory_objects(request, *args, **kwargs):
    category = kwargs["category"]
    sub_category = kwargs["sub_category"]

    try:
        products = Products.objects.get_product_by_sub_category(category=category, sub_category=sub_category)
    except Products.DoesNotExist:
        raise Http404("Not Found any Products in this Category!")

    context = {
        "object_list": products
    }

    return render(request, "productsList.html", context)


class SearchProducts(ListView):
    template_name = "productsList.html"
    model = Products
    paginate_by = 12

    def get_queryset(self):
        request = self.request
        query = request.GET.get("q")
        if query is not None:
            # print(Products.objects.search(query=query))
            return Products.objects.search(query=query)
        return redirect("products")


