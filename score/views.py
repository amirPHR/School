# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Import pagination in core app 
from core.pagination import DefaultPagination 

# Import serializers and models 
from .models import Score
from .serializers import ScoreSerializer

# Constants for Searching , Ordering and Default Ordering  
SEARCH_FILTER = ['student__user__username' , 'student__national_code' , 'student__phone_number']
ORDERING_FILTER = ['score' , 'date'] 
DEFAULT_ORDERING = ['id']

# Score ViewSet
class ScoreViewSet(ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = SEARCH_FILTER  
    ordering_fields = ORDERING_FILTER 
    ordering = DEFAULT_ORDERING 
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        user = self.request.user 
        if user.user_type in ['admin','teacher']:
            return super().get_queryset() 
        elif user.user_type == 'student':
            return super().get_queryset().filter(user=user)
    
    def create(self , request , *args , **kwargs):
        user = request.user
        if user.user_type in ['admin' , 'teacher']:
            return super().create(request , *args , **kwargs)
        else:
            return Response(
                {'detail':'You are not allow to create score.'}, 
                status = status.HTTP_403_FORBIDDEN
            )
    
    def update(self , request , *args , **kwargs):
        user = request.user
        if user.user_type in ['admin' , 'teacher']:
            return super().update(request , *args , **kwargs)
        else:
            return Response(
                {'detail':'You are not allow to create score.'}, 
                status = status.HTTP_403_FORBIDDEN
            )
            
    def destroy(self , request , *args , **kwargs):
        user = request.user
        if user.user_type in ['admin' , 'teacher']:
            return super().destroy(request , *args , **kwargs)
        else:
            return Response(
                {'detail':'You are not allow to create score.'}, 
                status = status.HTTP_403_FORBIDDEN
            )
            
    def partial_update(self , request , *args , **kwargs):
        user = request.user
        if user.user_type in ['admin' , 'teacher']:
            return super().partial_update(request , *args , **kwargs)
        else:
            return Response(
                {'detail':'You are not allow to create score.'}, 
                status = status.HTTP_403_FORBIDDEN
            )