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

# Import Permission_class from permission.py in user app
from .permission import CheckAdminPassword , IsAuthenticatedOrSignupOnly

# Constants for searching, and ordering
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
    permission_classes = [IsAuthenticatedOrSignupOnly, CheckAdminPassword]

    def get_queryset(self):
        """
        Custom queryset to return:
        - All data for admins.
        - Only the logged-in user's data for non-admins.
        """
        user = self.request.user
        if not user.is_authenticated:
            return self.request.none()
        return self.queryset if user.user_type == 'admin' else self.queryset.filter(id=user.id)

    def create(self, request, *args, **kwargs):
        """
        Override create method:
        - Prevent non-admin authenticated users from creating new users.
        - Allow unauthenticated users to sign up.
        """
        user = request.user 
        
        # Allow only admin to create new users
        if user.user_type == 'admin':
            return super().create(request, *args, **kwargs)
        
        # Prevent other authenticated users from creating new users
        return Response(
            {'detail': 'You are not allowed to create a new user.'},
            status=status.HTTP_403_FORBIDDEN
        )