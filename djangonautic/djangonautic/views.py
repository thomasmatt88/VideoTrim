from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('home')
    return render(request, 'index.html')

def trim(request):
    #if request.method == 'POST':
    #for i in request.POST.items():
    #    print(i)
    #(request.POST.items())
    #print(request.POST.get('test'))
    print(request.POST.getlist('mylist'))
    return render(request, 'index.html')
