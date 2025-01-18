# Import rest_framework libraries 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated

# Import models and serializers
from .models import Event 
from .serializers import EventSerializer 

# Import Pagination class from core app 
from core.pagination import DefaultPagination 

# Import Permission class from core app 
from core.permission import IsAdmin 

# Event ViewSet
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all() 
    serializer_class = EventSerializer 
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated, IsAdmin] 