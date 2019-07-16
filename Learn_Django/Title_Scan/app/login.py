# coding:utf-8

from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import Login
from .models import User
def home(request):
    reg = Login()
    return render(request,'login.html',{'forms':reg})

def login(request):
    if request.method == 'POST':
        do_login = Login(request.POST)
        if do_login.is_valid():
            username = do_login.cleaned_data['username']
            password = do_login.cleaned_data['password']
            try:
                login_obj = User.objects.filter(username=username).values()[0]
                if username == login_obj['username'] and password == login_obj['password']:
                    request.session['IS_LOGIN'] = True
                    return render(request,'tasks.html')
                else:
                    return HttpResponse('<h1>password error</h1>')
            except:
                return HttpResponse('<h1>database error</h1>')

    else:
        return render(request,'404.html')

