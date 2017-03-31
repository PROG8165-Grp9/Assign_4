from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from myTrans.models import Users

# Create your views here.
#def User_Log(request, id):
#    try:
#        UserId = User.objects.get(id=id)
#    except User.DoesNotExist:
#        raise Http404('User Does not Exist')
#    return render(request,'myTrans/Directory.html',{
#        'user':User.UserId
#    })

def myTrans(request):
    users = Users.objects
    return render(request,'myTrans/LogIn.html')
    #return HttpResponse('<p>In index view</p>')