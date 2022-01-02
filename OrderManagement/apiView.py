from django.http.response import Http404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, permissions
from django.http import HttpResponseRedirect, request
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.db.models import Q
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from .models import OrderCourse, Order
from .serializers import (OrderItemSerializer, OrderSerializer, 
                          BillingAddressSerializer, OrderItemForUserSerializer, 
                          OrderItemIdSerializer, CustomCourseSerializersForCheckOut)
from CourseManagement.serializers import CourseSerializersDemo
from CourseManagement.models import Course as CourseModel
from django.core import serializers



class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderCourse.objects.all()
    #authentication_classes = [TokenAuthentication]
    #authentication_classes = [SessionAuthentication]
    permission_classes = [ permissions.IsAuthenticated ]
    #permission_classes = [permissions.AllowAny]
    serializer_class = OrderItemSerializer
    #parser_classes = (MultiPartParser, FormParser,)

    def get_object(self, queryset=None, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            data = OrderCourse.objects.get(pk=pk,ordered=False)
            return data
        except:
            return Http404()

    def get_queryset(self):
        return OrderCourse.objects.all()

    def create(self, request, *args, **kwargs):
        """
        We will create a orderCourse objec with input of user form authentication
        and the item id from argument
        """

        try:
            order = Order.objects.get(user=request.user.id, ordered=False)
            db_data = order.items.filter(item_id=request.data.get('item'),ordered=False)
            print(f"-----------------> > >{ db_data } < < < -------------------")
            if(len(db_data) > 0):
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"-----------------> > >{e} < < < -------------------")
        
        try:
            
            data = {
            'user':request.user.id,
            'item': request.data.get('item'),
        }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        ret = self.perform_create(serializer)   
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        item = serializer.save()
        try:
            order = Order.objects.get(user=item.user, ordered=False)
        except:
            order = Order(user=item.user)
            order.save()
            
        order.items.add(item)
         
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()
            
class GetCoursesForCartIcon(APIView):
    """
    List all Order items that a user have,
    """
    #authentication_classes = [authentication.TokenAuthentication]
    #authentication_classes = [SessionAuthentication]
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderItemForUserSerializer

    def get(self, format=None, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user.id,ordered=False)
            orderItem = order.items.filter(ordered=False)
            serializer = self.serializer_class(orderItem, many=True)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckOutCoursesList(APIView):
    """
    List all Order items that a user have,
    """
    #authentication_classes = [authentication.TokenAuthentication]
    #authentication_classes = [SessionAuthentication]

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomCourseSerializersForCheckOut

    def get(self, format=None, *args, **kwargs):
        try:
            order = Order.objects.filter(user=self.request.user.id, ordered=False).last()
            order_ref = order.refrence_code
            ordered = order.items.values(
                'id', 'item__id', 'item__title', 'item__image', 
                'item__slug','item__price', 'item__discount_price', 'item__slug', 
                'item__description')
            
            serializer = self.serializer_class(ordered, many=True)
            data = {"course": serializer.data, "orderRef": order_ref}
            # ordered_CourseId = [i['item_id']for i in ordered]
            # ordered_itemId = [i['id']for i in ordered]
            # ordered_course = CourseModel.objects.filter(id__in=ordered_CourseId)
            # serializer = self.serializer_class(ordered_course, many=True)
            
            # order_item_id = OrderCourse.objects.filter(id__in=ordered_itemId)
            # serializer2 = OrderItemIdSerializer(order_item_id, many=True)
            # response = {"course": serializer.data, "id_list":serializer2.data}
            
        except Exception as e :
            return Response({e}, status=status.HTTP_200_OK)
            #rreturn Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class MyCoursesList(APIView):
    """
    List all Courses that a user have Enrolled,
    """
    #authentication_classes = [authentication.TokenAuthentication]
    #authentication_classes = [SessionAuthentication]

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomCourseSerializersForCheckOut

    def get(self, format=None, *args, **kwargs):
        try:
            orders = Order.objects.filter(user=self.request.user.id, ordered=True)
            data = []
            
            for order in orders: 
                ordered = order.items.values(
                    'id', 'item__id', 'item__title', 'item__image',
                    'item__slug', 'item__price', 'item__discount_price', 'item__slug',
                    'item__description')
                serializer = self.serializer_class(ordered, many=True)
                data.extend(serializer.data)
                
        except Exception as e:
            return Response({e}, status=status.HTTP_200_OK)
            #rreturn Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)



























# class SearchSuggestionCourse(APIView):
#     """
#     List all snippets, or create a new snippet.
#     You can add as much as functionality as you want for search.
#     """
#     #authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.AllowAny]
#     serializer_class = CourseSerializersTWO

#     def get(self, format=None, *args, **kwargs):
#         q = self.request.query_params.get('query', None)
#         courses = Course.objects.filter(Q(title__icontains=q))
#         data = self.serializer_class(courses, many=True)
#         return Response(data.data, status=status.HTTP_200_OK)


