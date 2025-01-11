# Import built-in libraries
from django.contrib import admin
from django.urls import path, include

# Import third-party libraries
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Import local app views
from user.views import UserViewSet
from student.views import StudentViewSet
from class_room.views import ClassRoomViewSet
from subject.views import SubjectViewSet 
from teacher.views import TeacherViewSet

# Admin site customization
admin.site.site_header = "School Management System"

# BaseRouter for registering ViewSets
router = DefaultRouter()
router.register(r'user', UserViewSet)  # User API
router.register(r'student', StudentViewSet)  # Student API
router.register(r'class_room', ClassRoomViewSet) # ClassRoom API
router.register(r'subject' , SubjectViewSet) # Subject API 
router.register(r'teacher' , TeacherViewSet) # Teacher API 

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="School Management API",
        default_version='v1',
        description="API documentation for the School Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@school.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Authentication routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Application routes
    path('user/', include('user.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('subject/', include('subject.urls')),
    path('class-room/', include('class_room.urls')),
    path('attendance/', include('attendance.urls')),
    path('score/', include('score.urls')),
    path('core/', include('core.urls')),

    # API ViewSets
    path('', include(router.urls)),
]