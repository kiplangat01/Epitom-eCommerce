from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Banner
class Banner(models.Model):
    img=models.CharField(max_length=200)
    all_text=models.CharField(max_length=300)
     

    class Meta:
        verbose_name_plural='1. Banners'


# category
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")
     
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title


# brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")

    def __str__(self):
        return self.title


# color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    def __str__(self):
        return self.title


# size
class Size(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)


    def __str__(self):
        return self.title


# product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveBigIntegerField()

    def __str__(self):
        return self.product.title

