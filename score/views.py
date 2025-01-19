# Import rest_framework libraries
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

# Import pagination in core app 
from core.pagination import DefaultPagination 

# Import Permission class from core app 
from core.permission import IsAdminOrTeacher

# Import serializers and models 
from .models import Score
from .serializers import ScoreSerializer , BadStudentSerializer 

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
    permission_classes = [IsAuthenticated, IsAdminOrTeacher]  
    
    def get_queryset(self):
        user = self.request.user 
        if user.user_type in ['admin','teacher']:
            return super().get_queryset()         
        return super().get_queryset().filter(student__user=user)
    
# Bad Student ViewSet
class BadStudentViewSet(ModelViewSet):
    """
    This View show students who has a bad score
    """
    queryset = Score.objects.filter(
        score__lte = 12,
        date_year = 'second_turn'
    )
    serializer_class = BadStudentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]