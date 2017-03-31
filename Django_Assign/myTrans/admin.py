from django.contrib import admin

# Register your models here.

from .models import User

class UserDetails(admin.ModelAdmin):
    list_display = ['Username','Email']

admin.site.register(User,UserDetails)