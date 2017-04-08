from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from myTrans.models import Transactions
from myTrans.forms import UserForm
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
    return render(request,'myTrans/Category.html')


