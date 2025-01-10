from django.contrib import admin 
from .models import Score 

@admin.register(Score) 
class ScoreAdmin(admin.ModelAdmin): 
    list_display = ['student' , 'subject' , 'score' , 'date' , 'disciplinery_status'] 
    list_filter = ['subject' , 'disciplinery_status'] 
    list_per_page = 10 
    ordering = ['id'] 
    search_fields = ['student__user__first_name' , 'student__user__last_name']