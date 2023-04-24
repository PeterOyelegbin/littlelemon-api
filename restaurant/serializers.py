from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="title", queryset=Category.objects.all())
    
    class Meta:
        model = MenuItem
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
