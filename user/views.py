# Import rest_framework libraries
import django_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from core.pagination import DefaultPagination 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.response import Response
# Import User Serializer
from .serializers import UserCreate
# Import User Model
from .models import User

# Filter Class for User
class FilterSetUser(django_filters.FilterSet):
    user_type = django_filters.CharFilter(field_name='user_type', lookup_expr='icontains')

# Permission Class for controlling access to views
class IsAuthenticatedOrSignupOnly(BasePermission):
    """
    Allows unauthenticated users to sign up, 
    but restricts authenticated users from performing certain actions.
    """
    def has_permission(self, request, view):
        if view.action == 'create':  # Allow signup action
            return True
        return request.user.is_authenticated  # Restrict others to authenticated users

# User ViewSet for handling CRUD operations
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreate
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['username', 'user_type']
    ordering = ['id']
    filterset_class = FilterSetUser
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticatedOrSignupOnly]

    # Custom get_queryset to return only the logged-in user's data
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.filter(id=self.request.user.id)
        return User.objects.none()

    # Override create method to prevent logged-in users from creating new users
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Provide a meaningful message if the user is not allowed to create new users
            return Response(
                {"message": "You are not allowed to create a new user."},
                status=status.HTTP_403_FORBIDDEN
            )
        # If the user is not authenticated, proceed with the regular create method
        return super().create(request, *args, **kwargs)