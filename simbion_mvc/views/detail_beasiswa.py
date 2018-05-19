from django.shortcuts import render

def detail_beasiswa(request, id_skema_beasiswa=None, id_skema_beasiswa_aktif=None):
    print('id skema beasiswa:', id_skema_beasiswa)
    print('id skema beasiswa aktif:', id_skema_beasiswa_aktif)
    return render(request, '4_info_beasiswa/index.html')
