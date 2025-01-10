# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

# Import pagination in core app
from core.pagination import DefaultPagination

# Import serializers and models
from .serializers import UserCreate
from .models import User

# Constants
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

# Custom Permissions
class IsAuthenticatedOrSignupOnly(BasePermission):
    """
    Custom permission class:
    - Allows unauthenticated users to sign up (create a new user).
    - Allows authenticated users to perform only authenticated operations.
    """
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user.is_authenticated

class CheckAdminPassword(BasePermission):
    """
    Custom permission to ensure the admin password is correct during user creation.
    """
    def has_permission(self, request, view):
        if view.action == 'create' and request.data.get("user_type") in ["admin", "teacher"]:
            return request.data.get("password") == '0960034455@gholampour'
        return True

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
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'admin':
                return self.queryset
            return self.queryset.filter(id=self.request.user.id)
        return self.queryset.none()

    def create(self, request, *args, **kwargs):
        """
        Override create method:
        - Prevent logged-in users (non-admin) from creating new users.
        - Allow unauthenticated users to sign up.
        """
        if request.user.is_authenticated and request.user.user_type in ['student', 'teacher']:
            return Response(
                {"message": "You are not allowed to create a new user."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Allow admins to create new users
        if request.user.is_authenticated and request.user.user_type == 'admin':
            return super().create(request, *args, **kwargs)

        # Allow unauthenticated users to sign up (create)
        return super().create(request, *args, **kwargs)