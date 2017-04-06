from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from myTrans import forms

from myTrans.models import Users

# Create your views here.

def myTrans(request):
    users = Users.objects
    return render(request,'myTrans/LogIn.html')
    #return HttpResponse('<p>In index view</p>')

def User_Log(request, username):
    users = Users.objects

    #try:
    #    UserId = Users.objects.get(Username=username)
    #except Users.DoesNotExist:
    #    raise Http404('User Does Not Exist')
    #return render(request, 'myTrans/Directory.html',{
    #    'user':Users.Username
    #})