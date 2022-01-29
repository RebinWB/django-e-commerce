import datetime
from django.db import models
from random import randint
from django.utils import timezone
from django.db.models import Q
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
import os

# rename gallery images
def rename_image(filepath):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    return name, ext

# gallery images uploader
def image_uploader(instance, filename):
    name, ext = rename_image(filename)
    pid = randint(1, 100)
    finalname = f"{instance.product.name}{pid}{ext}"
    return f"products/{instance.product.name}/{finalname}"

# base image rename
def rename_base_image(filepath):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    return name, ext

# base image Uploader
def base_image_uploader(instance, filename):
    name, ext = rename_image(filename)
    pid = randint(1, 100)
    finalname = f"products/{instance.name}{pid}{ext}"
    return f"{instance.name}/{finalname}"


class ProductsManager(models.Manager):
    """
    custom Products model manager
    """

    # return all products in the same category
    def get_product_by_category(self, category):
        result = self.get_queryset().filter(category__url__iexact=category)
        if result:
            return result
        raise Products.DoesNotExist

    # return all products in the same sub category
    def get_product_by_sub_category(self, category,  sub_category):
        result = self.get_queryset().filter(category__url__iexact=category, sub_category__url__iexact=sub_category)
        if result:
            return result
        raise Products.DoesNotExist

    # search engine with  
    def search(self, query):
        lookup = (
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__title__icontains=query) |
            Q(sub_category__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_available=True).distinct()


# ---------- Category Model ----------
class Category(models.Model):
    """
    products category model
    """
    title                   = models.CharField(max_length=150)
    url                     = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("categories", kwargs={"category": self.url})


def category_url_generator(sender, instance, created=False, *args, **kwargs):
    """
    generate unique slug for all Category instances url

    for example:
        Category title --> Men Category 
        Category url --> men-category
        Finally url --> <domain>/products/men-category/
    """
    if not instance.url:
        instance.url = slugify(instance.title)

pre_save.connect(category_url_generator, sender=Category)


# ---------- SubCategory Model ----------
class SubCategory(models.Model):
    """
    SubCategory model. SubCategory model is the subset of Category model 
    """
    title                   = models.CharField(max_length=150)
    url                     = models.CharField(max_length=150, blank=True)
    category_name           = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sub Categories"

    def get_absolute_url(self):
        return reverse("sub_categories", kwargs={"category": slugify(self.category_name.url), "sub_category": slugify(self.url)})


def sub_category_url_generator(sender, instance, created=False, *args, **kwargs):
    """
    generate unique slug for all SubCategory instances url

    for example:
        SubCategory title --> Women SubCategory 
        SubCategory url --> women-subcategory
        Finally url --> <domain>/products/<category>/women-subcategory/
    """
    if not instance.url:
        instance.url        = slugify(instance.title)

pre_save.connect(sub_category_url_generator, sender=SubCategory)

# ---------- Size Model ----------
class Size(models.Model):
    """
    Products Size model
    """
    title                   = models.CharField(max_length=150)

    def __str__(self):
        return self.title


# ---------- Products Model ----------
class Products(models.Model):
    """
    Products model
    """
    name                    = models.CharField(max_length=150)
    description             = models.TextField()
    image                   = models.ImageField(upload_to=base_image_uploader, null=True, blank=True)
    price                   = models.DecimalField(max_digits=7, decimal_places=2)
    size                    = models.ManyToManyField(Size)
    category                = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category            = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_available            = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(default=timezone.datetime.now)

    objects = ProductsManager()  # add Products Custom Manager functions to main Manager 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"product_id": self.id, "slug": slugify(self.name)})

    class Meta:
        verbose_name_plural = "Products"


# ---------- Products Gallery Model ----------
class Gallery(models.Model):
    """
    Gallery model. it's inline model for products model
    """
    image                   = models.ImageField(upload_to=image_uploader)
    product                 = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Galleries"
