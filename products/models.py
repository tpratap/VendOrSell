from django.db import models
from accounts.models import MyUser
from datetime import datetime
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.

# class Store(models.Model):
#     title = models.CharField(max_length=100, unique=True)
#     desc = models.CharField(max_length=500)
#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     seller_id = models.ForeignKey(MyUser, on_delete=models.PROTECT)
#     create_at = models.DateTimeField(auto_now_add=True)
category_choices = (
    ('books', 'Books'),
    ('electronics', 'Electronics Instruments'),
    ('furniture', 'Furniture'),
    ('apparels', 'Apparels'),
    ('other', 'Other')
)


# def upload_to(instance, filname):
#     return '{filename}'.format(filname=filname)


class Item(models.Model):
    title = models.CharField(max_length=100)
    desc = RichTextField()
    price = models.IntegerField()
    featured = CloudinaryField()
    sold = models.BooleanField(default=False)
    seller_id = models.UUIDField()
    category = models.CharField(max_length=50, choices=category_choices)
    bought = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)

# def get_path(instance, filename):
#     title = instance.item_id.title
#     item_id = str(instance.item_id)
#     return f'{title}/{item_id}/{filename}'

class ItemImg(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    itemImage = CloudinaryField()
