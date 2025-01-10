# Import rest_framework libraries
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Import pagination in core app
from core.pagination import DefaultPagination

# Import Student Serializer
from .serializers import StudentSerializer 

# Import Student Model 
from .models import Student 
from user.models import User 

# Constants 
SEARCH_FIELDS = ['national_code', 'phone_number', 'user__first_name', 'user__last_name'] 
ORDERING_FIELDS = ['class_room__base', 'class_room__field', 'id'] 
DEFAULT_ORDERING = ['user__username'] 

# Student ViewSet for handling CRUD operations
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = SEARCH_FIELDS 
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING 
    pagination_class = DefaultPagination 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Custom queryset:
        - Admin users can view all students.
        - Students can only view their own profile.
        """
        user = self.request.user

        if user.is_authenticated:
            # Admin users can view all students
            if user.user_type == 'admin':
                return super().get_queryset()

            # Students can view only their own profile
            if user.user_type == 'student':
                return super().get_queryset().filter(user=user)

        # If user is not authenticated, return an empty queryset
        return self.queryset.none()

        def create(self, request, *args, **kwargs):
            """
            Restrict students to only create profiles for themselves.
            """
            user = request.user

            # Prevent students from creating profiles for others
            if user.user_type == 'student':
                if 'user' in request.data and int(request.data['user']) != user.id:
                    return Response(
                        {"detail": "Students cannot create profiles for others."},
                        status=status.HTTP_403_FORBIDDEN
                    )

            return super().create(request, *args, **kwargs)