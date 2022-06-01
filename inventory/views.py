from django.shortcuts import render
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework .parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters
import os
# Create your views here.

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.object.all().order_by('create_at').reverse()
        serializer = ProductSerializer(products, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def product_by_id(request, id):
    try:
        product = Product.objects.get(pk = id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=201)

@csrf_exempt
def product_seller(request, seller_id):
    try:
        product = Product.objects.get(seller_id = seller_id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product, many = True)
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def productImg_list(request):
    if request.method == 'GET':
        ProductImgs = ProductImg.objects.all()
        serializer = ProductImgSerializer(ProductImgs, many = True)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductImgSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def productImg_by_id(request, id):
    try:
        productImg = ProductImg.objects.get(pk = id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductImgSerializer(productImg, many = True)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        productImg.delete()
        return HttpResponse(status=201)

# @csrf_exempt
# def productImg_by_product_id(request, id):
#     try:
#         productImg = ProductImg.objects.get(pk = id)
#     except:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = ProductImgSerializer(productImg, many = True)
#         return JsonResponse(serializer.data)
#     elif request.method == 'DELETE':
#         productImg.delete()
#         return HttpResponse(status=201)

@csrf_exempt
def product_by_category(request, category):
    try:
        product = Product.objects.filter(category = category)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product, many = True)
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def cart_list(request, category):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def cart_by_user_id(request, user_id):
    try:
        product = Cart.objects.filter(user_id = user_id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartSerializer(cart, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartSerializer(cart, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        cart.delete()
        return HttpResponse(status=201)


@csrf_exempt
def cart_item_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def cartItem_by_id(request, pk):
    try:
        cartItem = CartItem.objects.get(pk = pk)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializer(cartItem, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(cartItem, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        cartItem.delete()
        return HttpResponse(status=201)

@csrf_exempt
def cartItem_by_cart_id(request, cart_id):
    try:
        cartItem = CartItem.objects.filter(cart_id = cart_id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializer(cartItem, many = True)
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def cartItem_detect_same_product(request, cart_id, product_id):
    try:
        cartItem = CartItem.objects.filter(cart_id = cart_id).filter(product_id = product_id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializer(cartItem, many = True)
        return JsonResponse(serializer.data, safe = False)

class search_product(generics.ListAPIView):
    search_fields = ('product_name', 'category', 'desc')
    filter_backends = (filters.SearchFilter)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@csrf_exempt
def create_store(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonRespnse(serializer.errors, status = 400)

@csrf_exempt
def get_store(request, seller_id):
    try:
        store = Store.objects.filter(seller_id = seller_id)
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = StoreSerializer(store, many = True)
        return JsonRespnse(serializer.data, safe = False)

class upload_file(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


# def upload_file(request, seller_id):
#     try:
#         store = Store.objects.filter(seller_id = seller_id)
#     except:
#         return HttpResponse(status = 404)
#     if request.method == 'GET':
#         serializer = StoreSerializer(store, many = True)
#         return JsonRespnse(serializer.data, safe = False)

def delete_file(request, filename):
    if request.method == 'GET':
        ext = filename.split(".")[-1]
        filenameExt = filename.replace(f'{ext}',"")
        fileDir = "%s/%s.%s"("img", filenameExt, ext)
        if os.path.isfile((f'{img}/{filename}')):
            os.remove(fileDir)
            return HttpResponse(f'{filename} deleted')
        return HttpResponse('file not found')

def filter_range_price(request, minprice, maxprice):
    try:
        products = Product.objects.filter(price__range(minprice, maxprice))
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = ProductSerializer(products, many = True)
        return JsonResponse(serializer.data, safe = False)

def filter_min_price(request, minprice):
    try:
        products = Product.objects.filter(price__gte = minprice)
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = ProductSerializer(products, many = True)
        return JsonResponse(serializer.data, safe = False)

def filter_max_price(request, maxprice):
    try:
        products = Product.objects.filter(price__lte = maxprice)
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = ProductSerializer(products, many = True)
        return JsonResponse(serializer.data, safe = False)

def filter_rating(request, rating):
    try:
        products = Product.objects.filter(rating__gte = rating)
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = ProductSerializer(products, many = True)
        return JsonResponse(serializer.data, safe = False)


def filter_price_and_rating(request, minprice, maxprice, rating):
    try:
        products = Product.objects.filter(price_range(minprice,maxprice)).filter(rating__gte = rating)
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = ProductSerializer(products, many = True)
        return JsonResponse(serializer.data, safe = False)

def get_cart_item_by_cart_id(request, cart_id):
    try:
        cartItem = CartItem.objects.filter(cart_id = cart_id).prefetch_related('product_id').order_by('create_at')
    except:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = JoinSerializer(cartItem, many = True)
        return JsonResponse(serializer.data, safe = False)
