from django.shortcuts import render

def register_beasiswa(request):
    if request.method == 'POST':
        register_beasiswa_form(request)
    else:
        return render(request, '5_register_beasiswa/index.html')

def register_beasiswa_form(request):
    print(request.POST['ips'])


