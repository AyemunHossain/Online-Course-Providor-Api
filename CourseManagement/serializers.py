from rest_framework import serializers
from .models import Course, Category
from django.contrib.auth.models import User


   
class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',"title", "image", "image1", "image2", "image3", "price", "discount_price", "slug",
                  "description", "additional_info", "category", "featured")
    

class CourseSerializersDemo(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseSerializersForCheckOut(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('id',"title", "image", "price", "discount_price", "slug",
                  "description", "category")
        

class CourseSerializersTWO(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',"name","slug")

        
# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username','email')

# class UserSerializerWithToken(serializers.ModelSerializer):

#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)

#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_EN   CODE_HANDLER
#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
#         return token

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance


#     class Meta:
#         model = User
#         fields = ('token', 'username', 'password')

