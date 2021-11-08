from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def moments(request):
    return render(request, 'moments.html')