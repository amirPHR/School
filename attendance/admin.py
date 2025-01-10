from django.contrib import admin 
from .models import Attendance 

@admin.register(Attendance) 
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student' , 'date' , 'status'] 
    list_filter = ['status'] 
    list_per_page = 10 
    ordering = ['id'] 
    search_fields = ['student__user__first_name' , 'student__user__last_name' , 'student__national_code' , 'student__phone_number' , 'date']