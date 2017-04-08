from django.contrib import admin

# Register your models here.


from .models import Transactions

class UserDetails(admin.ModelAdmin):
   list_display = ['Username','Email']

class TransDetails(admin.ModelAdmin):
   list_display = ['id','Trans_Desc']

admin.site.register(Transactions,TransDetails)