from django.shortcuts import render

# Create your views here.
def func2(request):
    result=User.objects.all()
    return render(request,'app1.html',{'res':result})
