from django.db.models.query import QuerySet
from django.http.response import Http404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from CourseManagement.models import Course, Category
from rest_framework import viewsets, permissions
from .Serializers_Admin import CourseSerializersAdmin, CategorySerializers

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser


class CourseViewSet(viewsets.ModelViewSet):
    
    queryset = Course.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CourseSerializersAdmin
    parser_classes = ( MultiPartParser, FormParser,FileUploadParser, JSONParser)
    
    def get_object(self, queryset=None,**kwargs):
        var = self.kwargs.get('slug') or self.kwargs.get('pk')
        try:
            data = Course.objects.filter(pk=var).first()
            return data
        except:
            try:
                data = Course.objects.filter(slug=var).first()
                return data
            except:
                raise Http404()

    def get_queryset(self):
        return Course.objects.all()

    def create(self, request, *args, **kwargs):



        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        print(f"-----------------> > >{ serializer.errors} < < < -------------------")
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        course = serializer.save()

        try:
            for i in self.request.data['category']:
                if(i.isdigit()):
                    obj = Category.objects.get(pk=i)
                    course.category.add(obj)
        except:
            pass 
        
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    
class ListAllCategory(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializers

    def get(self, format=None, *args, **kwargs):
        try:
            queryset = Category.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            if(serializer.data):
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
           return Response(status=status.HTTP_204_NO_CONTENT)
