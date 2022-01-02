from django.contrib import admin
from .models import Order,OrderCourse,BillingAddress,Coupon,Payment


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user')


class OrderCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'item_id', 'ordered')
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderCourse, OrderCourseAdmin)
admin.site.register(BillingAddress)
admin.site.register(Coupon)
admin.site.register(Payment)
