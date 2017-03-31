from django.shortcuts import render
from django.http import Http404

from myTrans.models import User

# Create your views here.
def User_Log(request, id):
    try:
        UserId = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404('User Does not Exist')
    return render(request,'myTrans/Directory.html',{
        'user':User.UserId
    })