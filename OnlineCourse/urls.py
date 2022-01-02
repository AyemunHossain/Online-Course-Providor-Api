from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_swagger_view(title='Test All API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('CourseManagement.urls')),
    path('', include('UserManagement.urls')),
    path('api2/', include('OrderManagement.urls')),
    path('swagger/', schema_view),
    path('AdminApi/', include('AdminDashBoard.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
