from django.contrib import admin 
from .models import ReportCard 

@admin.register(ReportCard)
class ReportCardModel(admin.ModelAdmin):
    list_display = ['student' , 'calculate_average'] 
    list_display_links = ['student'] 
    list_filter = ['score'] 
    list_per_page = 10 
    search_fields = ['student__user__username', 'student__user__first_name' , 'student__national_code'] 