from django.shortcuts import render
from .models import WebSiteDetails

def about_configuration(request):
    details = None
    try:
        details = WebSiteDetails.objects.order_by("-id").first()
    except WebSiteDetails.DoesNotExist:
        pass

    context = {
        "details": details
    }

    return render(request, "about-us.html", context)
