from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers, urlpatterns
from .CourseManagement.ApiView_Admin import CourseViewSet, ListAllCategory
from .OrderManagement.ApiView_Admin import OrderViewSet_Admin
app_name = 'adminDashboard'

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, 'courses')
router.register('orders', OrderViewSet_Admin, 'orders')


urlpatterns = [
    path('', include((router.urls, 'adminCourseManagement'),
         namespace='adminCourseManagement')),
    path('category-list/', ListAllCategory.as_view(),name='list_all_category'),
    
]
