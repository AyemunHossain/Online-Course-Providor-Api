from .models import Course
from rest_framework import viewsets, permissions
from .serializers import CourseSerializers, CourseSerializersTWO
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.settings import api_settings
from django.shortcuts import get_object_or_404

# class CourseView
class CourseViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializers
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get_queryset(self):
        return Course.objects.all()
    
    def retrieve(self, request, pk=None):
        var = self.kwargs.get('slug') or self.kwargs.get('pk')
        try:
            obj = Course.objects.get(pk=var)
        except:
            try:
                obj = Course.objects.get(slug=var)
            except:
                obj ={}
        if(obj):
            serializer = self.serializer_class(obj)
            return Response(serializer.data)
        return Response([],status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
             return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


# class CourseView
class CoursesByCategory(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializers
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS


    def get(self,request, format=None, *args, **kwargs ):
        
        var = request.query_params.get('category')
        
        try:
            if(var.isdigit()):
                queryset = Course.objects.filter(
                    category__id=var)
            else:
                queryset = Course.objects.filter(
                    category__slug=var)
        except:
            queryset =[]
        
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.serializer_class(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class SearchCourse(APIView):
    """
    List all snippets, or create a new snippet.
    You can add as much as functionality as you want for search.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializers
    
    def get(self, format=None, *args, **kwargs ):
        q = self.request.query_params.get('query', None)    
        courses = Course.objects.filter(
            Q(title__icontains=q) | Q(category__name__icontains=q))
        data = self.serializer_class(courses, many=True)
        return Response(data.data , status=status.HTTP_200_OK)
    
class SearchSuggestionCourse(APIView):
    """
    List all snippets, or create a new snippet.
    You can add as much as functionality as you want for search.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializersTWO
    
    def get(self, format=None, *args, **kwargs ):
        q = self.request.query_params.get('query', None)
        courses = Course.objects.filter(
            Q(title__icontains=q) | Q(category__name__icontains=q))
        data = self.serializer_class(courses, many=True)
        return Response(data.data , status=status.HTTP_200_OK)