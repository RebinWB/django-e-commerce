from django.contrib import admin
from .models import (
    Products,
    Gallery,
    Category,
    SubCategory,
    Size
)

class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "category_name"
    ]

    list_filter = [
        "category_name",
    ]

class GalleryInlines(admin.TabularInline):
    model = Gallery
    max_num = 6

@admin.register(Products)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "is_available",
    ]

    inlines = [
        GalleryInlines
    ]

    list_editable = [
        "is_available"
    ]

    list_filter = [
        "is_available",
    ]

    search_fields = [
        "name",
        "description",
        "category",
        "sub_category",
    ]


admin.site.register(Size)
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryModelAdmin)
