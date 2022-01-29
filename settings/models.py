from django.db import models
from ckeditor.fields import RichTextField

def slider_image_uploader(instance, filename):
    """
    for example:
        'slider/black friday-12.png'
    """
    filename = f"{instance.title}-{instance.id}.png"
    return f"slider/{filename}"

class Slider(models.Model):
    """
    slider model 
    """
    title                   = models.CharField(max_length=150)
    url                     = models.URLField()
    image                   = models.ImageField(max_length=255, upload_to=slider_image_uploader)

    def __str__(self):
        return self.title


def banner_image_uploader(instance, filename):
    """
    for example:
        'banner/Large-black friday-12.png'
    """
    filename = f"{instance.banner_type}-{instance.title}-{instance.id}.png"
    return f"banner/{filename}"


BANNERS_TYPE = (
    ("Mini", "Mini"),
    ("Large", "Large"),
)

class Banner(models.Model):
    """
    mini banner is a small picture with a title and url that 
    will placed in below of slider. [Only the last three banners will be displayed]
    """
    title                   = models.CharField(max_length=150, blank=True, null=True)
    banner_type             = models.CharField(max_length=150, choices=BANNERS_TYPE, default="Mini")
    url                     = models.URLField(help_text="Example: https://mysite.com/products/...")
    image                   = models.ImageField(max_length=255, upload_to=banner_image_uploader)

    def __str__(self):
        return self.title


class WebSiteDetails(models.Model):
    """
    website information details model
    """
    title                   = models.CharField(max_length=60)
    description             = RichTextField(verbose_name="About Website")
    cover                   = models.ImageField(max_length=255, upload_to="about/CoverPost-image.png", blank=True, null=True, verbose_name="Cover Post")
    bg_cover                = models.ImageField(max_length=255, upload_to="about/background-image.png", blank=True, null=True, verbose_name="Back Ground")
    phone                   = models.CharField(max_length=60)
    email                   = models.EmailField()
    address                 = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Website Details"
