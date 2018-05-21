from django.shortcuts import render
from simbion_mvc.dao import donatur_dao,skema_beasiswa_dao
from simbion_mvc.entity import SkemaBeasiswa

def register_skema_beasiswa(request):
    return render(request, '3_register_skema_beasiswa/index.html')

@require_role(mahasiswa=False, admin=False, donatur=True)
def postRegisterBeasiswa(request):
    skema_baru = SkemaBeasiswa(donatur_dao.get_by_id(nomor_identitas_donatur), kode, nama, jenis, deskripsi)
    skema_beasiswa_dao.save(skema_baru)
    return render(reqiest, '3_register_skema_beasiswa/index.html')