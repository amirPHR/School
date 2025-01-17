from django.contrib import admin
from .models import Event , SignUpToEvent 

@admin.register(Event) 
class EventAdmin(admin.ModelAdmin):
    list_display = ['name' , 'description' , 'date'] 
    list_display_links = ['name'] 
    list_filter = ['name' , 'date'] 
    list_per_page = 10
    search_fields = ['date' , 'name'] 
    ordering = ['name']

@admin.register(SignUpToEvent) 
class SignUpToEventAdmin(admin.ModelAdmin):
    list_display = ['user' , 'event'] 
    list_display_links = ['user'] 
    list_filter = ['event'] 
    list_per_page = 10 
    search_fields = ['user__username', 'user__first_name' , 'user__last_name' , 'event'] 
    ordering = ['event']