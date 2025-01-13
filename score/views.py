# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Import pagination in core app 
from core.pagination import DefaultPagination 

# Import PermissionClass from permission in the score app
from .permission import RoleBasedPermission

# Import serializers and models 
from .models import Score
from .serializers import ScoreSerializer

# Constants for Searching , Ordering and Default Ordering  
SEARCH_FILTER = ['student__user__username' , 'student__national_code' , 'student__phone_number']
ORDERING_FILTER = ['score' , 'date'] 
DEFAULT_ORDERING = ['id']

# Score ViewSet
class ScoreViewSet(ModelViewSet):
    """
    ViewSet for managing Score records.
    Permissions and behavior are defined based on user roles.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = SEARCH_FILTER  
    ordering_fields = ORDERING_FILTER 
    ordering = DEFAULT_ORDERING 
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated , RoleBasedPermission]

    def get_queryset(self):
        """
        Return different querysets based on the user's role.
        Students can only access their own scores.
        Teachers and admins can access all scores.
        """
        user = self.request.user
        if user.user_type == 'student':
            return super().get_queryset().filter(student__user=user)
        if user.user_type in ['admin', 'teacher']:
            return super().get_queryset()
        return super().get_queryset().none()

    def check_permissions_for_action(self, user):
        """
        Check if the user has permission to perform the action.
        Returns error response if the user does not have the required role.
        """
        error_response = self.has_permission(user, ['teacher', 'admin'])
        if error_response:
            return error_response
        return None

    def create(self, request, *args, **kwargs):
        """
        Allow only teachers and admins to create scores.
        Students are not permitted to create scores.
        """
        user = request.user
        error_response = self.check_permissions_for_action(user)
        if error_response:
            return error_response
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Allow only teachers and admins to delete scores.
        Students cannot delete their scores.
        """
        user = request.user
        error_response = self.check_permissions_for_action(user)
        if error_response:
            return error_response
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Allow only teachers and admins to update scores.
        Students cannot update their scores.
        """
        user = request.user
        error_response = self.check_permissions_for_action(user)
        if error_response:
            return error_response
        return super().update(request, *args, **kwargs)