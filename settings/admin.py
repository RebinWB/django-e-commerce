from django.contrib import admin
from settings.models import Slider, Banner, WebSiteDetails


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "banner_type",
    ]


admin.site.register(Slider)
admin.site.register(WebSiteDetails)

