from rest_framework import serializers 
from .models import Teacher 

class TeacherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Teacher 
        fields = ['id' , 'user' , 'subject' , 'phone_number' , 'national_code' , 'birth_date' , 'date_add']