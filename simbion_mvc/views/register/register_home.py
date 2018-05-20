from django.shortcuts import render
from simbion_mvc.services.login import require_guest

@require_guest
def register(request):
    return render(request, '2_register/index.html')

@require_guest
def register_donatur(request):
    return render(request, '2_register/donatur.html')
