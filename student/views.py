# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# DefaultPagination in core app
from core.pagination import DefaultPagination  

# Import Permission from permission.py in student app
from .permission import IsStudentOrAdmin

# Import serializeres and models 
from .serializers import StudentSerializer  
from .models import Student  

# Constants for searching, and ordering
SEARCH_FIELDS = ['national_code', 'phone_number', 'user__username']
ORDERING_FIELDS = ['class_room__base', 'class_room__field']
DEFAULT_ORDERING = ['user__username']

# Student ViewSet
class StudentViewSet(ModelViewSet):
    """
    This is a Student API:
    - only students can create, delete, update their profiles here
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = SEARCH_FIELDS
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated , IsStudentOrAdmin]

    def get_queryset(self):
        """
        Custom queryset based on user type:
        - Admin: Can view all students.
        - Student: Can only view their own profile.
        """
        user = self.request.user
        
        if user.user_type != 'admin':
            return super().get_queryset().filter(user=user)
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        """ 
        Custom create method:
        - Restrict students to only create profiles for themselves.
        """
        user = request.user
        
        if user.user_type == 'student' and 'user' in request.data:
            if int(request.data['user']) != user.id:
                return Response(
                    {"detail": "Students cannot create profiles for others."},
                    status=status.HTTP_403_FORBIDDEN
                )

        return super().create(request, *args, **kwargs)