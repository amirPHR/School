from rest_framework import serializers 
from .models import Score 

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score 
        fields = ['id' , 'student' , 'subject' , 'score' , 'date' , 'disciplinery_status' , 'date_year'] 


class BadStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score 
        fields = ['student' , 'score' , 'subject' , 'disciplinery_status' , 'date_year']