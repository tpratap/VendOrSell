from django.db import models
from accounts.models import MyUser
from datetime import datetime
# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=256)
    seller_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=36)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=256)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name

class ProductImg(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)

class Cart(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey( Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

def upload_location(instance, filename):
    ext = filename.split(".")[-1]
    return "%s/%s.%s"%("img", datetime.now(), ext)

class FileUpload(models.Model):
    imgFile = models.ImageField(upload_to= upload_location)
