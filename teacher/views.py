# Import rest_framework libraries 
from rest_framework.viewsets import ModelViewSet 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.permissions import IsAuthenticated , BasePermission
from rest_framework.response import Response
from rest_framework import status

# Import serializers and models 
from .serializers import TeacherSerializer 
from .models import Teacher 
from user.models import User 

SEARCH_FIELDS = ['user__first_name' , 'user__last_name' , 'phone_number' , 'national_code']
ORDERING_FIELDS = ['subject']
DEFAULT_ORDERING = ['user__username']

class IsTeacher(BasePermission):
    def has_permission(self , request , view):
        user = request.user 
        if user.user_type in ['teacher' , 'admin']:
            return True 
        return False 

# TeacherViewSet
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = [SEARCH_FIELDS]
    ordering_fields = [ORDERING_FIELDS] 
    ordering = [DEFAULT_ORDERING]
    permission_classes = [IsAuthenticated , IsTeacher]
    
    def get_queryset(self):
        user = self.request.user 
        if user.user_type == 'admin':
            return super().get_queryset()
        if user.user_type == 'teacher':
            return super().get_queryset().filter(user=user) 
        return Teacher.objects.none()
    
    def create(self , request , *args , **kwargs):
        user = request.user 
        if user.user_type == 'teacher' and 'user' in request.data:
            if int(request.data['user']) != user.id:
                return Response({"detail":"Teachers cannot create profiles for others."} , status = status.HTTP_403_FORBIDDEN)
        return super().create(request , *args , **kwargs)