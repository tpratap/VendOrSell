from email.mime import image
import imp
from django.shortcuts import render
from datetime import date

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.mixins import DestroyModelMixin
from . import serializers
from .models import Item, ItemImg
from accounts.models import MyUser
# Create your views here.

class AddItem(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getItem(APIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ItemSerializer
    def get(self, request, format=None):
        try:
            id = request.query_params["id"]
            item = Item.objects.get(id = id)
            serializer = self.serializer_class(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {'detail': _('Id not available')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class deleteItem(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemSerializer
    def delete(self, request, id, format=None):
        try:
            # id = request.query_params["id"]
            seller_id = request.query_params["seller_id"]
            item = Item.objects.get(id = id)
            print(item)
            if str(seller_id) == str(item.seller_id):
                item.delete()
                return Response({}, status=status.HTTP_200_OK)
            else:
                content = {'detail': _('Seller_id not matched')}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        except:
            content = {'detail': _('Id not available')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
class getItems(APIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ItemSerializer
    def get(self, request, format=None):
        try:
            item = Item.objects.all()
            serializer = self.serializer_class(item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {'detail': _('Id not available')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class updateItem(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemSerializer
    def put(self, request, format=None):
        id = request.query_params["id"]
        seller_id = request.query_params["seller_id"]
        try:
            item = Item.objects.get(id = id)
            if str(seller_id) == str(item.seller_id):
                serializer = self.serializer_class(item, data=request.data, partial=True)
                if serializer.is_valid():
                    self.perform_update(serializer)
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    content = {'detail': _('Invalid data')}
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                content = {'detail': _('Seller_id not matched')}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        except:
            content = {'detail': _('Invalid data')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class getItem_by_Seller_id(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemSerializer
    def get(self, request, Format=None):
        try:
            seller_id = request.query_params["seller_id"]
            item = Item.objects.filter(seller_id = seller_id)
            serializer = self.serializer_class(item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {'detail': _('Items Not Found')}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

class ItemList(ListAPIView):
    queryset = Item.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.ItemSerializer
    pagination_class = PageNumberPagination
 

class AddItemImage(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemImageSerializer
    def post(self, request, format=None):
        item_id = request.data.get("item_id")
        seller_id = request.query_params["seller_id"]
        try:
            item = Item.objects.get(id = item_id)
            if str(seller_id) == str(item.seller_id):
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    try:
                        self.perform_create(serializer)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    except:
                        {'detail': _('Cannot Create')}
                        return Response(content, status=status.HTTP_400_BAD_REQUEST)
                else:
                    content = {'detail': _('Invalid Data')}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except:             
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getItemImages(APIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ItemImageSerializer
    def get(self, request, format=None):
        try:
            item_id = request.query_params["item_id"]
            item = Item.objects.filter(item_id = item_id)
            serializer = self.serializer_class(item, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {'detail': _('Id not available')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class getItemImage(APIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ItemImageSerializer
    def get(self, request, format=None):
        try:
            id = request.query_params["id"]
            item = Item.objects.filter(id = id)
            serializer = self.serializer_class(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {'detail': _('Id not available')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class deleteItemImages(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemImageSerializer
    def delete(self, request, item_id, format=None):
        try:
            seller_id = request.query_params["seller_id"]
            itemImages = ItemImg.objects.filter(item_id = item_id)
            item = Item.objects.filter(item_id=item_id)
            if str(seller_id) == str(item.seller_id):
                itemImages.delete()
                return Response({}, status=status.HTTP_200_OK)
            else:
                content = {'detail': _('Seller_id not matched')}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        except:
            content = {'detail': _('Id not available')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)