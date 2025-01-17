# Import rest_framework libraries 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status 

# Import models and serializers
from .models import Event , SignUpToEvent 
from .serializers import EventSerializer , SignUpToEventSerializer

# Event ViewSet
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all() 
    serializer_class = EventSerializer 
    permission_classes = [IsAuthenticated]
    
    def create(self , request , *args , **kwargs):
        """
        just admin can create events.
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to create event.'},
                status=status.HTTP_403_FORBIDDEN
            ) 
        return super().create(request , *args , **kwargs)
    
    
    def destroy(self , request , *args , **kwargs):
        """
        just admin can delete events.
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to delete event.'},
                status=status.HTTP_403_FORBIDDEN
            ) 
        return super().destroy(request , *args , **kwargs)
    
    
    def update(self , request , *args , **kwargs):
        """
        just admin can update events.
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to update event.'},
                status=status.HTTP_403_FORBIDDEN
            ) 
        return super().update(request , *args , **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        just admin can Partial update events.
        """
        user = request.user 
        if user.user_type != 'admin':
            return Response(
                {'detail':'You are not allow to update event.'},
                status=status.HTTP_403_FORBIDDEN
            ) 
        return super().partial_update(request , *args , **kwargs) 


# SignUp to Event ViewSet
class SignUpToEventViewSet(ModelViewSet):
    queryset = SignUpToEvent.objects.all()
    serializer_class = SignUpToEventSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        """
        users can only see their event
        """
        user = self.request.user 
        if user.user_type != 'admin':
            return super().get_queryset().filter(user=user) 
        return super().get_queryset() 
    
    def create(self, request, *args, **kwargs):
        """
        users can only signup for him/her self 
        """
        user = request.user
        if user.user_type != 'admin' and 'user' in request.data:
            if int(request.data['user']) != user.id:
                return Response(
                    {'detail':'You are not allow to sign up others in event.'},
                    status = status.HTTP_403_FORBIDDEN 
                )
        return super().create(request , *args , **kwargs)