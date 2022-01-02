from rest_framework import serializers
from CourseManagement.models import Course,Category


class CourseSerializersAdmin(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', "title", "image", "image1", "image2", "image3", "price", "discount_price", "slug",
                  "description", "additional_info", "featured")

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',"name","slug")
