from django.shortcuts import render

def login(request):
    return render(request, '1_login/index.html')
