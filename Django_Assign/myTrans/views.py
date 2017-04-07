from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Transaction
from .models import Users
=======
from myTrans import forms

from myTrans.models import Users
from myTrans.models import Transactions
>>>>>>> b335842f8aac28ab4af9a9c50ac8701c37e431df

# Create your views here.

def myTrans(request):
    #users = Users.objects
    #return render(request,'myTrans/LogIn.html')
    #return HttpResponse('<p>In index view</p>')
    Transac = Transactions.objects.exclude(Trans_Amnt=0)
    return render(request, 'myTrans/Directory.html', {
        'trans': Transac,
    })

def User_Log(request, username):
    users = Users.objects

    #try:
    #    UserId = Users.objects.get(Username=username)
    #except Users.DoesNotExist:
    #    raise Http404('User Does Not Exist')
    #return render(request, 'myTrans/Directory.html',{
    #    'user':Users.Username
    #})

<<<<<<< HEAD
def loadItems(request):
    items = Transaction.objects.all()
    return render(request,'myTrans/Directory.html', {
        'items': items,
    })

=======
def DashBoard_Load(request):
    Transac = Transaction.objects.exclude(Trans_Amnt=0)
    return render(request, 'myTrans/Directory.html', {
        'trans': Transac,
    })
>>>>>>> b335842f8aac28ab4af9a9c50ac8701c37e431df
