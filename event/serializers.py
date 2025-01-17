from rest_framework import serializers 
from .models import Event , SignUpToEvent 

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = ['name' , 'description' , 'date'] 

class SignUpToEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpToEvent 
        fields = ['user' , 'event']