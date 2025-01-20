# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser

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
    This is a ClassRoom API:
    - just admin can create, delete, update ClassRoom
    """
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING
    pagination_class = DefaultPagination
    permission_classes = [IsAdminUser]  