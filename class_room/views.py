# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

# Import Pagination class from core app
from core.pagination import DefaultPagination

# Import serializers and models
from .models import ClassRoom
from .serializers import ClassRoomSerializer

# Constants for Searching and Ordering
ORDERING_FIELDS = ['base', 'field']
DEFAULT_ORDERING = ['base']

# ClassRoom ViewSet
class ClassRoomViewSet(ModelViewSet):
    """
    ViewSet for managing ClassRoom data:
    - Allows only admin users to create and update.
    """
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING
    pagination_class = DefaultPagination
    permission_classes = [IsAdminUser]  

    def create(self, request, *args, **kwargs):
        """
        Override create method to restrict creation to admin users only.
        """
        if request.user.user_type != 'admin':
            return Response(
                {'detail': 'You are not allowed to create Class Room.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Override update method to restrict updates to admin users only.
        """
        if request.user.user_type != 'admin':
            return Response(
                {'detail': 'You are not allowed to update Class Room.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)