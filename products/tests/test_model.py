from django.test import TestCase
from products.models import (
                Products,
                Category,
                SubCategory,
                Size,
)

class TestModel(TestCase):

    def setUpTe(self):
        self.size = Size.objects.create(title="MM")
        self.image = "static/media-root/Boy Pants/products/Boy_Pants92.jpg"
        self.category = Category.objects.create(title="Men2")
        self.subcategory = SubCategory.objects.create(title="wen", category_name_id=self.category.id)
        self.product = Products.objects.create(
            name="product 1",
            description="hello baby",
            price=300.00,
            category=self.category,
            sub_category=self.subcategory,
            is_available=True,
            stock=120,
            image=self.image
        )


    # category url field generator Test
    # todo: create a category and return it's url field
    def test_category_url_generator(self):
        category1 = Category.objects.create(title="Category 1")
        self.assertEquals(category1.url, "category-1")

        category2 = Category.objects.create(title="Category 2")
        self.assertEquals(category2.url, "category-2")


    # sub category url field generator Test
    # todo: create a sub category and return it's url field
    def test_sub_category_get_absolute_url_generator(self):
        category1 = Category.objects.create(title="Category 1")
        self.assertEquals(category1.url, "category-1")

        category2 = Category.objects.create(title="Category 2")
        self.assertEquals(category2.url, "category-2")

        subcategory1 = SubCategory.objects.create(
            title="sub cateGory 1",
            category_name=category1
        )
        self.assertEquals(subcategory1.url, "sub-category-1")

        subcategory2 = SubCategory.objects.create(
            title="sub cateGory 2",
            category_name=category2
        )
        self.assertEquals(subcategory2.url, "sub-category-2")



