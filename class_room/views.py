# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser , BasePermission 
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

# Import serializers and models
from .models import ClassRoom 
from .serializers import ClassRoomSerializer 

ORDERING_FIELDS = ['base' , 'field'] 
DEFAULT_ORDERING = ['base']

# ClassRoom ViewSet
class ClassRoomViewSet(ModelViewSet):
    queryset = ClassRoom.objects.all() 
    serializer_class = ClassRoomSerializer
    filter_backends = [OrderingFilter , DjangoFilterBackend] 
    ordering_fields = ORDERING_FIELDS
    ordering = DEFAULT_ORDERING 
    permission_classes = [IsAdminUser] 