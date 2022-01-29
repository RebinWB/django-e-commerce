from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import ProductsList, product_details, return_category_objects, return_subcategory_objects


class TestUrls(SimpleTestCase):

    def test_product_url_resolve(self):
        url = reverse("products")
        self.assertEquals(resolve(url).func.view_class, ProductsList)

    def test_product_details_resolve(self):
        url = reverse("product_details", args=[1, "some-slug"])
        self.assertEquals(resolve(url).func, product_details)

    def test_product_category_resolve(self):
        url = reverse("categories", args=["some-slug"])
        self.assertEquals(resolve(url).func, return_category_objects)

    def test_product_sub_category_resolve(self):
        url = reverse("sub_categories", args=["some-slug", "some-slug"])
        self.assertEquals(resolve(url).func, return_subcategory_objects)
