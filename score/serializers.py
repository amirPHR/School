from rest_framework import serializers 
from .models import Score 

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score 
        fields = ['id' , 'student' , 'subject' , 'score' , 'date' , 'disciplinery_status' , 'date_year'] 


class BadStudentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    score = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    disciplinery_status = serializers.StringRelatedField() 
    date_year = serializers.StringRelatedField()
    
    class Meta:
        model = Score 
        fields = ['student' , 'score' , 'subject' , 'disciplinery_status' , 'date_year']