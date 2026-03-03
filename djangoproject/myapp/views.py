from django.shortcuts import render
from django.http import HttpResponse
from .models import Service

# Create your views here.

def index(request):
    # return HttpResponse('<h1>hello</h1>')
    ###dynamic input
    # name ='Ramesh'
    # return render(request,'index.html',{'name':name})
    # ##better use like this
    # context ={
    #     'name':'Ramesh',
    #     'age':20,
    # }
    # return render(request,'index.html',context)
    service1 = Service()
    service1.id = 1
    service1.name = 'web dev'
    service1.details = "Crafting responsive, modern websites that deliver exceptional user experiences and drive business growth."
    service1.is_true = True

    service2 = Service()
    service2.id = 2
    service2.name = 'Brand Design'
    service2.details = "Creating compelling visual identities that communicate your brand's essence and resonate with your audience."
    service2.is_true = False

    service3 = Service()
    service3.id = 3
    service3.name = 'Digital Marketing'
    service3.details = "Strategic marketing solutions that amplify your reach and convert prospects into loyal customers."
    service3.is_true = True

    service4 = Service()
    service4.id = 4
    service4.name = 'Mobile Apps'
    service4.details = "Native and cross-platform mobile applications that provide seamless functionality across all devices."
    service4.is_true = True

    Services = [service1,service2,service3,service4]


    return render(request,'index.html' ,{'Services':Services})

def counter(request):
    text = request.POST['text']
    amount_of_words= len(text.split())
    return render(request, 'counter.html',{'amount':amount_of_words})