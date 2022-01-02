from django.http.response import Http404
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from OrderManagement.models import Order, OrderCourse
from .Serializers_Admin import OrderItemForUserSerializer_Admin, OrderSerializer_Admin

class OrderViewSet_Admin(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = OrderSerializer_Admin
    parser_classes = (JSONParser,)

    def get_object(self, queryset=None,**kwargs):
        var = self.kwargs.get('refrence_code') or self.kwargs.get('pk')
        try:
            data = Order.objects.get(pk=var)
            return data
        except:
            try:
                data = Order.objects.get(refrence_code=var)
                return data
            except:
                raise Http404()

    def get_queryset(self):
        return Order.objects.all()

    #599232v9oc6e
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
