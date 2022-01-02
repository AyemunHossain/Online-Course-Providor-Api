
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .apiView import (OrderItemViewSet, GetCoursesForCartIcon,
                      CheckOutCoursesList, MyCoursesList)
    
from .PaymentApiView import StripeCheckoutView, StripePaymentStatusView
app_name = 'orderManagement'


router = routers.DefaultRouter()
router.register('cart', OrderItemViewSet,'add_to_cart')
# router.register('checkout', OrderViewSet, 'checkout_from_cart')


urlpatterns = [
    path('', include((router.urls, 'orderManagementApi'),namespace='orderManagement')),
    path('cart-icon-course/', GetCoursesForCartIcon.as_view(),name='cart_course_for_user'),
    path('checkout-courses/', CheckOutCoursesList.as_view(), name='cart_items'),
    path('my-courses/', MyCoursesList.as_view(), name='my_courses'),
    path('strip-payment/', StripeCheckoutView.as_view(), name='strip_payment'),
    path('strip-payment-status-check/',StripePaymentStatusView.as_view(), name='strip_payment_status_check'),
]
