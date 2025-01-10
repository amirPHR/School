from django.contrib import admin
from .models import Subject 

@admin.register(Subject) 
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    list_per_page = 10 
    ordering = ['name']