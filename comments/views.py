from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.text import slugify
from accounts.models import Account
from products.models import Products
from .forms import CommentForm
from .models import Comment

def product_comment(request):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        user_id = comment_form.cleaned_data["user_id"]
        product_id = comment_form.cleaned_data["product_id"]
        comment_text = comment_form.cleaned_data["comment_text"]

        # creating comment in database and send it to management system
        # todo: create comment with received data
        user = Account.objects.get(id=user_id)
        product = Products.objects.get(id=product_id)
        comment = Comment.objects.create(
            user=user,
            product=product,
            text=comment_text
        )
        comment.save()

        # todo: re-new comment form
        comment_form = CommentForm()

        return redirect(f"products/{product.id}/{slugify(product.name)}")

    return HttpResponse("You Are not Login")
