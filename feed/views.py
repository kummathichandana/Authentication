from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def func(request):
    result=User.objects.all()
    return render(request,'index.html',{'res':result})