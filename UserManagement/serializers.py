from rest_framework import serializers
from django.conf import settings
from UserManagement.models import UserAccount




class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('email','username','password')
        extra_kwargs = {'password' : {'write_only':True}} 
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserDetailsForNav(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    auth   = serializers.BooleanField(default=False)
    admin = serializers.BooleanField(default=False)
    email = serializers.CharField(max_length=200)
    avatar = serializers.ImageField(allow_null=True)