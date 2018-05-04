from django.shortcuts import render

# Create your views here.
def index(request, page=None):
    return render(request, 'index.html', {'page': page})
