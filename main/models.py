from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_images/")


    def __str__(self):
        return self.title
