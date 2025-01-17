from rest_framework import serializers 
from .models import Student
from user.models import User 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ['id' , 'user' , 'father_name' , 'national_code' , 'birth_date' , 'phone_number' , 'address' , 'class_room' , 'date_add']

    def validation_national_code(self , value): 
        """         
        This validation check:
        - National code just digits. 
        - National code just 10 digits
        """
        if not value.isdigit():
            raise serializers.ValidationError('National code must contain only digits.')
        if len(value) != 10:
            raise serializers.ValidationError('National code must be exactly 10 digits.') 
        return value 