from django.http import HttpResponse
from django.shortcuts import render

from .videotrim import videotrim

def home(request):
    #return HttpResponse('home')
    return render(request, 'index.html')

def trim(request):
    #if request.method == 'POST':
    video_file_path = request.POST.get('video_file_path')
    videotrim(video_file_path, request.POST.getlist('mylist'))
    return render(request, 'index.html')
