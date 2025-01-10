from rest_framework import serializers 
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ['user' , 'father_name' , 'national_code' , 'birth_date' , 'phone_number' , 'address' , 'class_room' , 'date_add']