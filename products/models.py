import os
import random

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse

# from desSyabil.aws.download.utils import AWSDownload
# from desSyabil.aws.utils import ProtectedS3Storage
from desSyabil.utils import unique_slug_generator

LABEL_CHOICES = (
    ('N', 'new'),
    ('B', 'bestseller'),
    ('C', 'clearance'),
)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category", kwargs={"name": self.name})


class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sub-Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category", kwargs={"name": self.name})


class Brand(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__title__icontains=query)
                   )
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):  # Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)

    # category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, blank=False, on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, blank=True)
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.CASCADE)

    price = models.DecimalField(decimal_places=2, max_digits=5, default=19.99)
    discount_price = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    description = models.TextField(default="Empty description")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    quantity = models.IntegerField(default=10)
    featured = models.BooleanField(default=False)

    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_digital = models.BooleanField(default=False)  # User Library

    objects = ProductManager()

    class Meta:
        ordering = ("title",)

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def get_image_url(self):
        try:
            url = self.image.url
        except Exception:
            url = ''
        return url

    def __str__(self):
        return self.title

    @property
    def is_available(self):
        return self.quantity > 0

    @property
    def name(self):
        return self.title

    # def get_downloads(self):
    #     qs = self.productfile_set.all()
    #     return qs


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)


def upload_product_file_loc(instance, filename):
    slug = instance.product.slug
    # id_ = 0
    id_ = instance.id
    if id_ is None:
        Klass = instance.__class__
        qs = Klass.objects.all().order_by('-pk')
        if qs.exists():
            id_ = qs.first().id + 1
        else:
            id_ = 0
    if not slug:
        slug = unique_slug_generator(instance.product)
    location = "product/{slug}/{id}/".format(slug=slug, id=id_)
    return location + filename  # "path/to/filename.mp4"

# class ProductFile(models.Model):
#     product = models.ForeignKey(Product)
#     name = models.CharField(max_length=120, null=True, blank=True)
#     file = models.FileField(
#         upload_to=upload_product_file_loc,
#         storage=ProtectedS3Storage(),  # FileSystemStorage(location=settings.PROTECTED_ROOT)
#     )  # path
#     # filepath        = models.TextField() # '/protected/path/to/the/file/myfile.mp3'
#     free = models.BooleanField(default=False)  # purchase required
#     user_required = models.BooleanField(default=False)  # user doesn't matter
#
#     def __str__(self):
#         return str(self.file.name)
#
#     @property
#     def display_name(self):
#         og_name = get_filename(self.file.name)
#         if self.name:
#             return self.name
#         return og_name
#
#     def get_default_url(self):
#         return self.product.get_absolute_url()
#
#     def generate_download_url(self):
#         bucket = getattr(settings, 'AWS_STORAGE_BUCKET_NAME')
#         region = getattr(settings, 'S3DIRECT_REGION')
#         access_key = getattr(settings, 'AWS_ACCESS_KEY_ID')
#         secret_key = getattr(settings, 'AWS_SECRET_ACCESS_KEY')
#         if not secret_key or not access_key or not bucket or not region:
#             return "/product-not-found/"
#         PROTECTED_DIR_NAME = getattr(settings, 'PROTECTED_DIR_NAME', 'protected')
#         path = "{base}/{file_path}".format(base=PROTECTED_DIR_NAME, file_path=str(self.file))
#         aws_dl_object = AWSDownload(access_key, secret_key, bucket, region)
#         file_url = aws_dl_object.generate_url(path, new_filename=self.display_name)
#         return file_url
#
#     def get_download_url(self):  # detail view
#         return reverse("products:download",
#                        kwargs={"slug": self.product.slug, "pk": self.pk}
#                        )
