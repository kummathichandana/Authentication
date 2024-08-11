from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



def loginView(request):
    if request.method=="POST":
        #result=User.objects.all()
        usern=request.POST.get('lion')
        passw=request.POST.get('goat')
        check=User.objects.filter(username=usern).exists()
        print(check)
    return render(request,'login.html')

def homeView(request):
    return render(request,'home.html')

def aboutView(request):
    return render(request,'about.html')

def contactView(request):
    return render(request,'contact.html')

def postView(request):
    return render(request,'post.html')
def userView(request):
    return render(request,'user.html')



def userView(request):
    result = None
    if request.method == "POST":
        usern = request.POST.get('name')
        if usern:  # Check if 'name' was provided
            result = User.objects.filter(username=usern)
            # If you want to check if any users exist:
            exists = result.exists()
            print(exists)  # This is for debugging purposes; consider using logging in production
        return render(request, 'user.html', {'res': result})
    
    # For GET requests, or if POST data is not available:
    return render(request, 'user.html')
