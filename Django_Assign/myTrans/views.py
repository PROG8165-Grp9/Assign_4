from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from myTrans.models import Transactions
from myTrans.models import Category
from myTrans.forms import UserForm
from myTrans.forms import CategoryForm
# Create your views here.

def loadItems(request):
    items = Transactions.objects.exclude(Trans_Amnt=0)
    return render(request,'myTrans/Directory.html', {
        'items': items,
})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('loadItems')
    else:
        form = UserForm()
    return render(request, 'myTrans/SignUp.html', {'form': form})


def loadCategory(request):
    items = Category.objects.exclude()
    return render(request,'myTrans/Category.html', {
        'items': items,
    })


def categoryView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Cate_Type = form.cleaned_data.get('Cate_Type')
            Cate_Desc = form.cleaned_data.get('Cate_Desc')
            form = Category(Cate_Type=Cate_Type, Cate_Desc=Cate_Desc)
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    return render(request, 'myTrans/AddCategory.html', {'form': form})



def newTransaction(request):
    return render(request,'myTrans/NewTransaction.html')