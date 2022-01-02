
from django.conf.urls import include
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from UserManagement.apiView import (
    NewUserCreate,
    BlacklistTokenAdding,
    GetUserStatusAndDetails
)

app_name = 'usermanagement'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/register/', NewUserCreate.as_view(), name="register_new_user"),
    path('api/user-status/', GetUserStatusAndDetails.as_view(),name="is_authenticated_user"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/blacklist/', BlacklistTokenAdding.as_view(), name='blacklist'),
]
