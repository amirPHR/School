from django.contrib import admin 
from .models import Teacher 

@admin.register(Teacher) 
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user' , 'subject' , 'phone_number' , 'national_code' , 'birth_date']
    list_filter = ['subject']
    list_per_page = 10 
    ordering = ['id'] 
    search_fields = ['user__first_name' , 'user__last_name' , 'phone_number' , 'national_code']