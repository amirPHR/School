from django.contrib import admin
from .models import Event 

@admin.register(Event) 
class EventAdmin(admin.ModelAdmin):
    list_display = ['name' , 'description' , 'date'] 
    list_display_links = ['name'] 
    list_filter = ['name' , 'date'] 
    list_per_page = 10
    search_fields = ['date' , 'name'] 
    ordering = ['name']