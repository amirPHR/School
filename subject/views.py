# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated , BasePermission
from rest_framework.response import Response 
from rest_framework import status 

# Import pagination in core app 
from core.pagination import DefaultPagination

# Import serializers and models 
from .serializers import SubjectSerializer 
from .models import Subject 

# Constants for searching, and ordering
SEARCH_AND_ORDERING_FIELDS = ['name']

# Subject ViewSet 
class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all() 
    serializer_class = SubjectSerializer
    pagination_class = DefaultPagination
    filter_backends = SearchFilter , OrderingFilter
    search_fields = SEARCH_AND_ORDERING_FIELDS 
    ordering = SEARCH_AND_ORDERING_FIELDS
    permission_classes = [IsAuthenticated]
    
    def create(self , request , *args , **kwargs):
        user = request.user 
        if user.user_type in ['admin']:
            return super().create(request , *args , **kwargs) 
        return Response(
            {'detail':'You are not allow to create subject.'},
            status = status.HTTP_403_FORBIDDEN
        )
    
    def destroy(self , request , *args , **kwargs):
        user = request.user 
        if user.user_type in ['admin']:
            return super().destroy(request , *args , **kwargs) 
        return Response(
            {'detail':'You are not allow to create subject.'},
            status = status.HTTP_403_FORBIDDEN
        )
    
    def update(self, request, *args, **kwargs):
        user = request.user
        if user.user_type in ['admin']:
            return super().update(request , *args , **kwargs) 
        return Response(
            {'detail':'You are not allow to update subject.'},
            status = status.HTTP_403_FORBIDDEN
        )
    
    def partial_update(self, request, *args, **kwargs):
        user = request.user
        if user.user_type in ['admin']:
            return super().partial_update(request , *args , **kwargs) 
        return Response(
            {'detail':'You are not allow to update subject.'},
            status = status.HTTP_403_FORBIDDEN
        )