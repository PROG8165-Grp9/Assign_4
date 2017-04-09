from django.contrib import admin

# Register your models here.


from .models import Transactions
from .models import Category

class UserDetails(admin.ModelAdmin):
   list_display = ['Username','Email']

class TransDetails(admin.ModelAdmin):
   list_display = ['id','Trans_Desc']

class CateDetails(admin.ModelAdmin):
   list_display = ['id','Cate_Type', 'Cate_Desc']


admin.site.register(Transactions,TransDetails)
admin.site.register(Category,CateDetails)