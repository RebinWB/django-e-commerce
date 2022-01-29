from django.contrib import messages
from django.shortcuts import render

from accounts.models import Account
from contact.forms import ContactForm
from contact.models import Contact
from settings.models import WebSiteDetails


def contact_view(request):
    if request.user.is_authenticated:
        user = Account.objects.get(id=request.user.id)
        contact_form = ContactForm(request.POST or None, initial={"fullname": user.username, "email": user.email})
    else:
        contact_form = ContactForm(request.POST or None)

    if contact_form.is_valid():
        fullname = contact_form.cleaned_data.get("fullname")
        email = contact_form.cleaned_data.get("email")
        subject = contact_form.cleaned_data.get("subject")
        message = contact_form.cleaned_data.get("message")

        new_contact = Contact.objects.create(name=fullname, email=email, subject=subject, message=message)
        new_contact.save()
        messages.success(request, "your message sent successfully", "success")

    details = None
    try:
        details = WebSiteDetails.objects.order_by("-id").first()
    except WebSiteDetails.DoesNotExist:
        pass

    context = {
        "contact_form": contact_form,
        "details": details
    }

    return render(request, "contact-us.html", context)
