# Import rest_framework libraries 
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status

# DefaultPagination in core app
from core.pagination import DefaultPagination  

# Import permission class from teacher app
from .permissions import IsTeacherOrAdmin

# Import serializers and models 
from .serializers import TeacherSerializer 
from .models import Teacher 

# Constants for Searching , Ordering , Deafault Ordering
SEARCH_FIELDS = ['user__username' , 'phone_number' , 'national_code' , 'user__first_name' , 'user__last_name']
ORDERING_FIELDS = ['subject']
DEFAULT_ORDERING = ['user__username']

# TeacherViewSet
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = SEARCH_FIELDS
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING
    permission_classes = [IsAuthenticated , IsTeacherOrAdmin]
    
    def get_queryset(self):
        """
        Custom queryset:
        - Admin: Access to all teachers.
        - Teacher: Access to their own profile only.
        """
        user = self.request.user
        if user.user_type == 'admin':
            return super().get_queryset()
        else:
            return super().get_queryset().filter(user=user)
            
    def create(self, request, *args, **kwargs):
        """
        Custom create method:
        - Admin: Can create profiles for others.
        - Teachers: Can only create profiles for themselves.
        """
        user = request.user
        if user.user_type == 'teacher' and 'user' in request.data:
            if int(request.data['user']) != user.id:
                return Response(
                    {'detail': 'You are only allowed to create a profile for other.'},
                    status=status.HTTP_403_FORBIDDEN
                )
        return super().create(request, *args, **kwargs)