from django.http import HttpResponse
from django.shortcuts import render
from . import models

from .scan import Info_Scan

def Add_Task(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            run_scan_model(url)
            return HttpResponse('<script>alert("ADD SUCCESS,PLEASE WAIT A MINUTES")</SCRIPT>')
        except:
            return HttpResponse('<script>alert("SAME URL")</SCRIPT>')
    else:
        return render(request,'404.html')

def Del_Task(request):
    try:
        models.Tasks.objects.all().delete()
    except Exception as e:
        print(e)
    return HttpResponse('<script>alert("Delete Success")</SCRIPT>')


import threading
def scan_model(url):
    result = Info_Scan(url).Get_Result()
    print(result)
    data_commit = models.Datas(title=result[1],power=result[2],ip=result[3],open_port=str(result[4]))
    data_commit_1 = models.Tasks(url=url)
    data_commit_1.save()
    data_commit.uid = data_commit_1
    data_commit.save()

def run_scan_model(url):
    t = threading.Thread(target=scan_model,args=(url,))
    print('Scan_Model is running....')
    t.start()
