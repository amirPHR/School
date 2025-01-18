from rest_framework import serializers 
from .models import ClassRoom 

# ClassRoom Serializer
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom 
        fields = ['base' , 'field']