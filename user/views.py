# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status

# Import pagination in core app
from core.pagination import DefaultPagination

# Import serializers and models
from .serializers import UserCreate
from .models import User

# Constants for searching , ordering and DefaultOrdering
SEARCH_FIELDS = ['username', 'email', 'first_name', 'last_name']
ORDERING_FIELDS = ['username', 'user_type']
DEFAULT_ORDERING = ['username']

# Filter Class for User
class UserFilterSet(filters.FilterSet):
    """
    FilterSet for filtering User.
    """
    user_type = filters.CharFilter(field_name='user_type', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['user_type']

# User ViewSet
class UserViewSet(ModelViewSet):
    """
    ViewSet for managing User data:
    - Allows users to view, create, and filter their data.
    - Restricts actions based on authentication status.
    """
    queryset = User.objects.all()
    serializer_class = UserCreate
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = SEARCH_FIELDS
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING
    filterset_class = UserFilterSet
    pagination_class = DefaultPagination
    
    def get_queryset(self): 
        """
        Users can only see their profiles.
        """
        user = self.request.user 
        if user.is_authenticated:
            if user.user_type == 'admin':
                return super().get_queryset()
            return super().get_queryset().filter(id=user.id) 
        return super().get_queryset().none()
    
    def create(self , request , *args, **kwargs):
        user_type = request.data.get('user_type') 
        password = request.data.get('password')
        """
        permission for admin password   
        """
        if user_type in ['admin' , 'teacher']:
            if password != '0960034455@gholampour':
                return Response(
                    {'detail':'Password is incorrect'},
                    status = status.HTTP_403_FORBIDDEN)
            return super().create(request , *args, **kwargs)    
        """
        permission for student password.
        """
        if user_type == 'student':
            if password != '111111g01':
                return Response(
                    {'detail':'Password is incorrect'},
                    status = status.HTTP_403_FORBIDDEN 
                )
            return super().create(request, *args, **kwargs)