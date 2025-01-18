from rest_framework import serializers 
from .models import ReportCard 

class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard 
        fields = ['student' , 'score' , 'calculate_average']