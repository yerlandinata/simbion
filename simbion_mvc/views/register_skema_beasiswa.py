from django.shortcuts import render
from simbion_mvc.dao import donatur_dao,skema_beasiswa_dao
from simbion_mvc.entity import SkemaBeasiswa
from simbion_mvc.services.login import require_role

def register_skema_beasiswa(request):
    return render(request, '3_register_skema_beasiswa/index.html')

@require_role(mahasiswa=False, admin=False, donatur=True)
def postRegisterBeasiswa(request):
    if(request.method == 'POST'):
        nomor_identitas_donatur = 1 #DUMMY DATA
        kode = request.POST['kode']
        nama = request.POST['nama_beasiswa']
        jenis = request.POST['jenis']
        deskripsi = request.POST['deskripsi']
        skema_baru = SkemaBeasiswa(donatur_dao.get_by_id(nomor_identitas_donatur), kode, nama, jenis, deskripsi)
        skema_beasiswa_dao.save(skema_baru)
    
    return render(request, '3_register_skema_beasiswa/index.html')