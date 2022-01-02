from rest_framework import routers, urlpatterns
from .apiView import *
from django.urls import path, include

app_name = 'coursemanagement'

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, 'courses')


urlpatterns = [
    path('', include((router.urls, 'coursemanagementapi'),namespace='coursemanagement')),
    path('courses-search/', SearchCourse.as_view(), name='search_course'),
    #path('courses/', CourseViewSet.as_view(), name='courses'),
    path('courses-by-category/', CoursesByCategory.as_view(), name='course_by_category'),
    
    path('courses-search/suggestion/', SearchSuggestionCourse.as_view(), name='search_suggestion_course'),
]








# path('user/', CurrentUser.as_view()),
# path('user-list/', UserList.as_view())
