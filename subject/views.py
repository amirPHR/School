# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet 
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated , BasePermission
from rest_framework.response import Response 
from rest_framework import status 

# Import pagination in core app 
from core.pagination import DefaultPagination

# Import serializers and models 
from .serializers import SubjectSerializer 
from .models import Subject 
from user.models import User 
        

SEARCH_AND_ORDERING_FIELDS = ['name']
# Subject ViewSet 
class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all() 
    serializer_class = SubjectSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter , OrderingFilter] 
    search_fields = [SEARCH_AND_ORDERING_FIELDS] 
    ordering = [SEARCH_AND_ORDERING_FIELDS] 
    permission_classes = [IsAuthenticated]
    
    def create(self , request , *args , **kwargs):
        user = request.user 
        if user.is_authenticated and user.user_type in ['student' , 'teacher']:
            return Response({'message':'You can not create subject.'} , status = status.HTTP_403_FORBIDDEN)  
        return super().create(request , *args , **kwargs)
    
    def destroy(self , request , *args , **kwargs):
        user = request.user 
        if user.user_type in ['student' , 'teacher']:
            return Response({'message':'You can not delete the subject.'} , status = status.HTTP_403_FORBIDDEN)
        return super().destroy(request , *args , **kwargs)
    
    def update(self, request, *args, **kwargs):
        user = request.user
        if user.user_type in ['student', 'teacher']:
            return Response({'message': 'You are not allowed to update this data.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        user = request.user
        if user.user_type in ['student', 'teacher']:
            return Response({'message': 'You are not allowed to update this data.'}, status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)