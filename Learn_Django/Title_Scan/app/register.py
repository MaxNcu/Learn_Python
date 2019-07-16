from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from .forms import Register
from .models import User

def home(request):
    reg = Register()
    return render(request,'register.html',{'forms':reg})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            User.objects.create(username=username,password=password,email=email)
            return HttpResponse('<h1>Register Success</h1>')
        except:
            return render(request,'404.html')
    else:
        return render(request,'404.html')