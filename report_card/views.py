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

# Import Pagination class from core app 
from core.pagination import DefaultPagination 

# Constants for Searching and Ordering 
SEARCHE_FILTER = ['student__user__username', 'student__national_code']
ORDERING_FILTER = ['calculate_average', 'score']

# ReportCard ViewSet
class ReportCardViewSet(ModelViewSet):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 
    pagination_class = DefaultPagination
    search_fields = SEARCHE_FILTER 
    ordering_fields = ORDERING_FILTER 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        just teachers and admins can see ReportCard of all students.
        students just can see their ReportCard.
        """
        user = self.request.user 
        if not user.user_type in ['admin']:
            return super().get_queryset().filter(student__user=user)  
        return super().get_queryset()
    
    def create(self , request , *args , **kwargs):
        """
        just admins can create ReportCards
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to create Report Card.'},
                status = status.HTTP_403_FORBIDDEN 
            )
        return super().create(request, *args, **kwargs) 
    
    def destroy(self , request , *args , **kwargs):
        """
        just admins can delete ReportCards
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to delete Report Card.'},
                status = status.HTTP_403_FORBIDDEN 
            )
        return super().destroy(request, *args, **kwargs) 
    
    def update(self , request , *args , **kwargs):
        """
        just admins can update ReportCards
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to update Report Card.'},
                status = status.HTTP_403_FORBIDDEN 
            )
        return super().update(request, *args, **kwargs) 
    
    def partial_update(self , request , *args , **kwargs):
        """
        just admins can partial_update ReportCards
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to update Report Card.'},
                status = status.HTTP_403_FORBIDDEN 
            )
        return super().partial_update(request, *args, **kwargs) 