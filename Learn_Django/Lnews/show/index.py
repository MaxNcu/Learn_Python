from django.shortcuts import render
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .models import News_Data

def index(requests):
    # paginator = Paginator(News_Data.objects.all().values(),5)
    # print(paginator)
    # page = requests.GET['page']
    # try:
    #     news_result = paginator.page(page)
    # except PageNotAnInteger:
    #     news_result = paginator.page(1)
    # except EmptyPage:
    #     news_result = paginator.page(paginator.num_pages)
    # return render(requests,'index.html',{'news_result':news_result})

    return render(requests,'index.html')

def login_index(requests):
    return render(requests,'login.html')

def register_index(requests):
    return render(requests,'register.html')
