from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import serializers, viewsets, permissions
from .serializers import RegisterUserSerializer, UserDetailsForNav
from django.http import response
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
import json
from rest_framework_simplejwt.tokens import RefreshToken, Token
from UserManagement.models import UserProfile
from django.shortcuts import get_object_or_404


class NewUserCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format='json'):
        reqNserializer = RegisterUserSerializer(data=request.data)

        if reqNserializer.is_valid():
            try:
                newUser = reqNserializer.save()
                if newUser:
                    response = reqNserializer.data
                    return Response(response, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(reqNserializer.errors or None, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenAdding(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format='json'):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetUserStatusAndDetails(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        auth = request.user.is_authenticated
        if(auth):
            try:
                avatar = get_object_or_404(
                    UserProfile, user__id=request.user.id).avatar
            except:
                avatar = None
            admin = request.user.is_admin
            content = {
                'auth': auth,
                'admin': admin,
                'username': request.user.username,
                'email': request.user.email,
                'avatar': avatar
            }
            serializer = UserDetailsForNav(data=content)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            

# class CurrentUser(APIView):
#     permission_classes =(permissions.IsAuthenticated,)
#     def post(self, request, format=None):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

# class UserList(APIView):

#     permission_classes = (permissions.AllowAny,)

#     def get(self, request, format=None):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def post(self, request, format=None):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
