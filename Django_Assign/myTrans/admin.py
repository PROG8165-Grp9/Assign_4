from django.contrib import admin

# Register your models here.

from .models import Users
from .models import Transaction

class UserDetails(admin.ModelAdmin):
   list_display = ['Username','Email']

class TransDetails(admin.ModelAdmin):
   list_display = ['id','Trans_Desc']

admin.site.register(Users,UserDetails)
admin.site.register(Transaction,TransDetails)