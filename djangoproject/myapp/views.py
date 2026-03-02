from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>hello</h1>')
    ###dynamic input
    # name ='Ramesh'
    # return render(request,'index.html',{'name':name})
    # ##better use like this
    context ={
        'name':'Ramesh',
        'age':20,
    }
    return render(request,'index.html',context)