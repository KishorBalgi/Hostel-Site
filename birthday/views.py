from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')