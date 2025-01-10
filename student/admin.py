from django.contrib import admin 
from .models import Student 

@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user' , 'father_name' , 'national_code' , 'birth_date' , 'phone_number' , 'address' , 'class_room'] 
    list_filter = ['user' , 'class_room']
    list_per_page = 10 
    ordering = ['id'] 
    search_fields = ['user__first_name' , 'user__last_name' , 'national_code' , 'phone_number']