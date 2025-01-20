# Import rest_framework libraries 
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status 

# Import serializers and models
from .serializers import ReportCardSerializer 
from .models import ReportCard 

# Import Permission class from permissions.py 
from core.permission import IsAdmin 

# Import Pagination class from core app 
from core.pagination import DefaultPagination 

# Constants for Searching and Ordering 
SEARCHE_FILTER = ['student__user__username', 'student__national_code']
ORDERING_FILTER = ['calculate_average', 'score']

# ReportCard ViewSet
class ReportCardViewSet(ModelViewSet):
    """
    This is a ReportCard API:
    - just admin can create, delete, update ReportCard
    - Student just can see thei ReportCard
    """
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 
    pagination_class = DefaultPagination
    search_fields = SEARCHE_FILTER 
    ordering_fields = ORDERING_FILTER 
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        """
        just teachers and admins can see ReportCard of all students.
        students just can see their ReportCard.
        """
        user = self.request.user 
        if not user.user_type in ['admin']:
            return super().get_queryset().filter(student__user=user)  
        return super().get_queryset()