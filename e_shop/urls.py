from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from e_shop import settings
from e_shop.settings import DEBUG
from e_shop.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('', include("products.urls")),
    path('', include("accounts.urls")),
    path('', include("comments.urls")),
    path('', include("orders.urls")),
    path('', include("coupon.urls")),
    path('', include("wishlist.urls")),
    path('', include("settings.urls")),
    path('', include("contact.urls")),


    # API URLS
    path('api/accounts/', include("accounts.api.urls")),
    path('api/comment/', include("comments.api.urls")),
    path('api/contact/', include("contact.api.urls")),
    path('api/coupon/', include("coupon.api.urls")),
    path('api/orders/', include("orders.api.urls")),
    path('api/products/', include("products.api.urls")),
    path('api/wishlist/', include("wishlist.api.urls")),
]

if DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
