from pyexpat import model
from products.models import Item, ItemImg
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'desc', 'featured', 'price', 'seller_id', 'category', 'bought', 'create_at')



class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImg
        fields = ('id', 'item_id', 'itemImage')
