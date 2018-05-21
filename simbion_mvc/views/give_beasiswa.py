from django.shortcuts import render
from simbion_mvc.dao import pendaftaran_dao,mahasiswa_dao,skema_beasiswa_dao,skema_beasiswa_aktif_dao


def give_beasiswa(request):
    response = {}
    pendaftaran = pendaftaran_dao.getAll()
    response['table_content'] = pendaftaran
    return render(request, '6_give_beasiswa/index.html',response)
