from django.contrib import admin 
from .models import User 

@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'password' , 'user_type']
    list_filter = ['user_type']
    list_display_links = ['username']
    list_per_page = 10 
    ordering = ['id']
    search_fields = ['username', 'email'] 