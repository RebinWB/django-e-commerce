from django.test import TestCase, Client
from django.urls import reverse
from products.models import Products, Category, SubCategory, Size


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.size = Size.objects.create(title="MM")
        self.image = "static/media-root/Boy Pants/products/Boy_Pants92.jpg"
        self.category = Category.objects.create(title="Men2")
        self.subcategory = SubCategory.objects.create(title="wen", category_name_id=self.category.id)
        self.product = Products.objects.create(
            name="product1",
            description="hello baby",
            price=300.00,
            category=self.category,
            sub_category=self.subcategory,
            is_available=True,
            stock=120,
            image=self.image
        )
        self.list_url = reverse("products")
        self.detail_url = reverse("product_details", args=[self.product.id, self.product.name])
        self.category_url = reverse("categories", args=[self.product.category])
        self.subcategory_url = reverse("sub_categories", args=[self.product.category, self.product.sub_category])

    def test_product_list_view(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "productsList.html")

    def test_product_detail_view(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "productDetails.html")

    def test_product_by_category_view(self):
        response = self.client.get(self.category_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "productsList.html")

    def test_product_by_sub_category_view(self):
        response = self.client.get(self.subcategory_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "productsList.html")
