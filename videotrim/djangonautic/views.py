from django.http import HttpResponse
from django.shortcuts import render

from .videotrim import videotrim

video_file_path = '/Users/matthewthomas/Downloads/IMG_4135.MOV'

def home(request):
    #return HttpResponse('home')
    return render(request, 'index.html')

def trim(request):
    #if request.method == 'POST':
    #print(request.POST.getlist('mylist'))
    videotrim(video_file_path, request.POST.getlist('mylist'))
    return render(request, 'index.html')
