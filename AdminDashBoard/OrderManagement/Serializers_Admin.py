from rest_framework import serializers
from OrderManagement.models import Order,OrderCourse


class OrderItemForUserSerializer_Admin(serializers.ModelSerializer):
    class Meta:
        model = OrderCourse
        fields = "__all__"


class OrderSerializer_Admin(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
