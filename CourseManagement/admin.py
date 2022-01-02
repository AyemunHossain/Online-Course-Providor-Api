from django.contrib import admin
from CourseManagement.models import Course,Category


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Category)

