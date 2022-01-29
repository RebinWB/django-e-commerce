from django import template
from django.template.defaultfilters import safe

from settings.models import WebSiteDetails

register = template.Library()


@register.simple_tag
def footer_description():
    description = None
    try:
        description = WebSiteDetails.objects.get_queryset().first().description
    except WebSiteDetails.DoesNotExist:
        pass

    return safe(description)


@register.simple_tag
def footer_phone():
    phone_number = None

    try:
        phone_number = WebSiteDetails.objects.order_by("-id").first().phone
    except WebSiteDetails.DoesNotExist:
        pass

    return phone_number


@register.simple_tag
def footer_address():
    address = None

    try:
        address = WebSiteDetails.objects.order_by("-id").first().address
    except WebSiteDetails.DoesNotExist:
        pass

    return address


@register.simple_tag
def footer_email():
    email = None

    try:
        email = WebSiteDetails.objects.order_by("-id").first().email
    except WebSiteDetails.DoesNotExist:
        pass

    return email

