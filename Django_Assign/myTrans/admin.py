from django.contrib import admin

# Register your models here.

from .models import Users

class UserDetails(admin.ModelAdmin):
   list_display = ['Username','Email']

admin.site.register(Users,UserDetails)