from django.contrib import admin 
from .models import ClassRoom 

@admin.register(ClassRoom) 
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['base' , 'field'] 
    list_per_page = 10 
    ordering = ['id'] 