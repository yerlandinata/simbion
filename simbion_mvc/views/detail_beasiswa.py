from django.shortcuts import render
from simbion_mvc.dao import skema_beasiswa_dao,skema_beasiswa_aktif_dao,syarat_beasiswa_dao
response = {}
def detail_beasiswa(request,id_skema_beasiswa, id_skema_beasiswa_aktif):
    print('id skema beasiswa:', id_skema_beasiswa)
    print('id skema beasiswa aktif:', id_skema_beasiswa_aktif)
    
    skema_beasiswa = skema_beasiswa_dao.get_by_kode(id_skema_beasiswa)
    data = skema_beasiswa_aktif_dao.get_by_skema_beasiswa_and_no_urut(skema_beasiswa,id_skema_beasiswa_aktif) 
    syarat = syarat_beasiswa_dao.get_by_kode(id_skema_beasiswa)
    response['syarat'] = syarat
    response['beasiswa'] = data
    response['id_skema_beasiswa'] = id_skema_beasiswa
    response['id_skema_beasiswa_aktif'] = id_skema_beasiswa_aktif
    return render(request, '4_info_beasiswa/detail_beasiswa.html', response)