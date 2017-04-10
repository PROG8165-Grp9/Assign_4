from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category
from .models import Transactions

class UserForm(UserCreationForm):
    # to take the input of username
    username = forms.CharField(max_length=100)
    # to take the input of email
    email = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Cate_Type', 'Cate_Desc']

class AddTransForm():
    class Meta:
        model = Transactions
        fields = ['Trans_Desc', 'Trans_Date', 'Trans_Type', 'Trans_Loc', 'Trans_Amnt', ]