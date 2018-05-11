from django.shortcuts import render

def info_beasiswa(request):
    return render(request, 'landing/index.html')
