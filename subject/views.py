# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated

# Import pagination in core app 
from core.pagination import DefaultPagination

# Import Permission class from permissions.py
from core.permission import IsAdmin 

# Import serializers and models 
from .serializers import SubjectSerializer 
from .models import Subject 

# Constants for searching, and ordering
SEARCH_AND_ORDERING_FIELDS = ['name']
    
# Subject ViewSet 
class SubjectViewSet(ModelViewSet):
    """
    This is a Subject API:
    - only admin can create, delete, update subjects 
    """
    queryset = Subject.objects.all() 
    serializer_class = SubjectSerializer
    pagination_class = DefaultPagination
    filter_backends = SearchFilter , OrderingFilter
    search_fields = SEARCH_AND_ORDERING_FIELDS 
    ordering = SEARCH_AND_ORDERING_FIELDS
    permission_classes = [IsAuthenticated, IsAdmin]