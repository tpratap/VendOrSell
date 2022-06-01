from django.urls import include, path
from .views import *
 
urlpatterns = [
	path('showItemCart/<int:cart_id>', get_cart_item_by_cart_id),
    path('store/', create_store),
    path('store/<int:user_id>', get_store),
    path('product/', product_list),
    path('product/find', search_product.as_view()),
    path('product/<int:pk>', product_by_id),
    path('product/seller/<int:seller_id>', product_seller),
    path('cart/',cart_list),
    path('cart/<int:user_id>', cart_by_user_id),
    path('cartItem/', cart_item_list),
    path('cartItem/<int:cart_id>', cartItem_by_cart_id),
    path('cartItem/id/<int:pk>/', cartItem_by_id),
    path('cartItemDetectSameItem/<int:cartId>/<int:productId>/', cartItem_detect_same_product),
    path('productImg/', productImg_list),
   # path('productImg/<int:productId>/', productImg_product_id),
    path('productImg/id/<int:id>/', productImg_by_id),
    path('product/find/<str:category>/', product_by_category),
    path('uploadFile/', upload_file.as_view()),
    path('deleteFile/<str:filename>/', delete_file),
    path('filter/price/<int:minprice>/<int:maxprice>/', filter_range_price),
    path('filter/price/min/<int:minprice>/',filter_min_price),
    path('filter/price/max/<int:maxprice>/', filter_max_price),
    path('filter/rating/<int:rating>/', filter_rating),
]