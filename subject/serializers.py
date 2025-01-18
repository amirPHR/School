from rest_framework import serializers 
from .models import Subject 

# Subject Serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject 
        fields = ['id' , 'name']