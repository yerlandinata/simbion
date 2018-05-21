from django.shortcuts import render,HttpResponseRedirect
from simbion_mvc.dao import skema_beasiswa_dao,skema_beasiswa_aktif_dao,mahasiswa_dao,pendaftaran_dao
from simbion_mvc.services.login import require_role
from django.core.exceptions import EmptyResultSet

def register_beasiswa(request, id_skema_beasiswa=1, id_skema_beasiswa_aktif=1):
    response ={}
    skema = skema_beasiswa_dao.get_by_kode(id_skema_beasiswa)
    skema_aktif = skema_beasiswa_aktif_dao.get_by_skema_beasiswa_and_no_urut(skema, id_skema_beasiswa_aktif)
    response['skema_default'] = skema_aktif
    response['skema'] = skema_beasiswa_aktif_dao.getall()
    response['npm'] = '219550888271'
    if request.method == 'POST':
        print("POST")
        return register_beasiswa_form(request,id_skema_beasiswa,id_skema_beasiswa_aktif,response)
    else:
        print("Get")
        return render(request, '5_register_beasiswa/index.html',response)

@require_role(mahasiswa=True)
def register_beasiswa_form(request,id_skema_beasiswa,id_skema_beasiswa_aktif,response={}):
    print(request.POST['ips'])
    check = validate(request.POST['npm'],id_skema_beasiswa,id_skema_beasiswa_aktif,request.POST['ips'])
    if check:
        response['success'] = True
        return render(request,'5_register_beasiswa/success_mendaftar.html')
    else:
        return render(request,'5_register_beasiswa/index.html',response)

def validate(npm,kode_skema,no_urutSkema,ips):
    print(ips)
    if not ips:
        print("IPS False")
        return False
    try:
        mahasiswa = mahasiswa_dao.get_by_npm(npm)
        skema = skema_beasiswa_dao.get_by_kode(kode_skema)
        skema_beasiswa_aktif = skema_beasiswa_aktif_dao.get_by_skema_beasiswa_and_no_urut(skema,no_urutSkema)
    except EmptyResultSet:
        print("Cant empty")
        return False
    try:
        cek_mahasiswa = pendaftaran_dao.get_by_npm(mahasiswa)
        cek_beasiswa_aktif = pendaftaran_dao.get_by_skema_beasiswa_and_no_urut(skema_beasiswa_aktif)
    except EmptyResultSet:
        print("What we want , perfect")
        return True
    return False



