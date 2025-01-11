# Import rest_framework libraries
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated , BasePermission
from rest_framework.response import Response
from rest_framework import status

# DefaultPagination in core app
from core.pagination import DefaultPagination  

# Import serializeres and models 
from .serializers import StudentSerializer  
from .models import Student  
from user.models import User  

# Constants for searching, and ordering
SEARCH_FIELDS = ['national_code', 'phone_number', 'user__first_name', 'user__last_name' , 'user__username']
ORDERING_FIELDS = ['class_room__base', 'class_room__field', 'id']
DEFAULT_ORDERING = ['user__username']

class IsStudent(BasePermission):
    def has_permission(self , request , view):
        user = request.user 
        if user.user_type in ['student' , 'admin']:
            return True 
        return False 
    
class StudentViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD operations on Student model.
    Includes filtering, searching, ordering, and permission control.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = SEARCH_FIELDS
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated , IsStudent]

    def get_queryset(self):
        """
        Custom queryset based on user type:
        - Admin: Can view all students.
        - Student: Can only view their own profile.
        """
        user = self.request.user
        
        # Admin can see all students. 
        if user.user_type == 'admin':
            return super().get_queryset()
        
        #students just can see their profile.  
        if user.user_type == 'student':
            return super().get_queryset().filter(user=user)

        return self.queryset.none()

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