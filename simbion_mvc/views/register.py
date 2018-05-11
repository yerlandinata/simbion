from django.shortcuts import render

def register(request):
    return render(request, '2_register/index.html')

def register_mahasiswa(request):
    return render(request, '2_register/mahasiswa.html')

def register_donatur(request):
    return render(request, '2_register/donatur.html')

def register_donatur_individual(request):
    return render(request, '2_register/donatur-individual.html')

def register_donatur_yayasan(request):
    return render(request, '2_register/donatur-yayasan.html')
