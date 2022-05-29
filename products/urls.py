from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add_item/', views.AddItem.as_view(), name='add-item'),
    path('get_item/', views.getItem.as_view(), name='get-item'),
    path('delete_item/<int:id>/', views.deleteItem.as_view(), name='delete-item'),
    path('get_items/', views.getItems.as_view(), name='get-items'),
    path('list/', views.ItemList.as_view(), name='items'),
    path('update_item/', views.updateItem.as_view(), name='update-item'),
    path('add_item_images/', views.AddItemImage.as_view(), name='add-item-images'), 
    path('get_item_images/', views.getItemImages.as_view(), name='get-item-images'),
    path('delete_item_images/<int:item_id>/', views.deleteItemImages.as_view(), name='delete-item-images'),
    path('get_item_image/', views.getItemImage.as_view(), name='get-item-image'),   
    path('my_items/', views.getItem_by_Seller_id.as_view(), name='get-items-by-seller-id'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
