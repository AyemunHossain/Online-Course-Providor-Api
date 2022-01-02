from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import OrderCourse, Order, BillingAddress, Coupon
from CourseManagement.models import Category, Course

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCourse
        fields = (
                    'id',
                   'user',
                  'item',
                  'ordered',
                  )
        read_only_fields=('id','ordered')


class OrderItemIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCourse
        fields = (
            'id',
        )
        read_only_fields = ('id',)


class OrderItemForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCourse
        fields = (
            'user',
            'id',
            'item',
            'ordered',
        )
        read_only_fields = ('id','item','ordered',)
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user',
                  'items',
                  'refrence_code',
                  'start_date',
                  'ordered_completion_date',
                  'ordered',
                  'billing_address',
                  'coupon',
                  'payment_status'
                  )


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        models = BillingAddress
        fields = ('user',
                  'address',
                  'apartment_address',
                  'zipcode',
                  'save_info')
        
        
class CustomCourseSerializersForCheckOut(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    item__id = serializers.IntegerField( read_only=True)
    item__title = serializers.CharField(max_length=450, required=False)
    item__image = serializers.SlugField(allow_blank=True, allow_unicode=False, max_length=50, required=False)
    item__price = serializers.DecimalField(decimal_places=2,max_digits=20, min_value=0.0, required=False)
    item__discount_price = serializers.DecimalField(allow_null=True, decimal_places=2, max_digits=20, min_value=0.0, required=False)
    item__slug = serializers.SlugField(allow_blank=True, allow_unicode=False, max_length=50, required=False)
    item__description = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    #item__category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:

        fields = ('id', 'item__id', "item__title", "item__image", "item__price", "item__discount_price", "item__slug",
                  "item__description",)
