from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import News_Data,User


def show(requests):
    try:
        paginator = Paginator(News_Data.objects.all().values(),5)
        page = requests.GET['page']
        counts = paginator.count
        try:
            news_result = paginator.page(page)
        except PageNotAnInteger:
            news_result = paginator.page(1)
        except EmptyPage:
            news_result = paginator.page(paginator.num_pages)
        return render(requests,'show.html',{'news_result':news_result,'counts':counts})
    except:
        return render(requests,'404.html')
global_keyword = ''
def search(requests):
    try:
        try:
            keyword = requests.POST['keyword']
        except:
            keyword = requests.GET['keyword']
        page = requests.GET.get('page',2)
        datas = News_Data.objects.filter(title__icontains=keyword).values()
        print(datas)
        counts = len(datas)
        if len(datas) == 0:
            return render(requests,'404.tml')
        if len(datas) <6:
            page_count = len(datas)
        else:
            page_count = 5
        paginator = Paginator(datas,page_count)
        try:
            news_result = paginator.page(page)
        except PageNotAnInteger:
            news_result = paginator.page(1)
        except EmptyPage:
            news_result = paginator.page(paginator.num_pages)
        return render(requests, 'show.html', {'news_result': news_result,'keyword':keyword,'counts':counts})
    except Exception as e:
        print(e)
        return render(requests,'404.html')
def register(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username,password=password)
        return HttpResponse(content='<script>alert("Register Success")</script>',status=222)
    except:
        return render(request,'404.html')


def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        Check_Loing = User.objects.get(username=username)
        if Check_Loing.username == username and Check_Loing.password == password:
            request.session['username'] = username
        return HttpResponse('<script>alert("LOGIN SUCCESS")</script>')
    except:
        raise render(request,'404.html')


