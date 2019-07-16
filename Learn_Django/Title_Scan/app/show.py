# coding:utf-8
from .models import Datas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Comment

def show(request):
    is_login = request.session.get('IS_LOGIN',False)
    if not is_login:
        return render(request, '404.html')

    paginator = Paginator(Datas.objects.all().values(),3)
    # 获取到数据的对象，按照每页5个
    # paginator.count
    # # 获取到的数据的总数
    # paginator.num_pages
    # # 获取的页数
    # paginator.object_list
    # 和 Datas.objects.all() 返回的结果一致
    #------------------------------------#
    # page1 = paginator.page(1)
    # page1.object_list
    # 即 Datas.objects.all() 取第一个结果
    # page1.next_page_number()
    # 获取下一页的页码，如果不存在则会报错
    # page1.previous_page_number
    # 获取上一页的页码，如果不存在则会报错
    comment = Comment()
    print(comment)
    page = request.GET.get('page')
    # 获取前端传递过来的page参数
    try:
        beatles_list = paginator.page(page)
    except PageNotAnInteger: # 如果 page 参数不为正整数，显示第一页
        beatles_list = paginator.page(1)
    except EmptyPage: # 如果 page 参数为空页，跳到最后一页
        beatles_list = paginator.page(paginator.num_pages)
    return render(request,'show.html',{'bea_list':beatles_list,'comment':comment})

