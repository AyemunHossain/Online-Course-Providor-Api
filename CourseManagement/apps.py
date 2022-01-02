from django.apps import AppConfig


class CoursemanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CourseManagement'

    def ready(self):
        import CourseManagement.signals
