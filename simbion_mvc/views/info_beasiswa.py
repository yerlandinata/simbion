from django.shortcuts import render

response = {}
def info_beasiswa(request):
    beasiswa_list = [{'nama':'yumna','tgl_tutup_pendaftaran':'9/11/2019','jumlah_pendaftar':93,'id_skema_beasiswa':'KJ307','id_skema_beasiswa_aktif':'bbbbb'},{'nama':'yumni','tgl_tutup_pendaftaran':'9/11/2019','jumlah_pendaftar':93}]
    #ToDo IMPLEMENT METHOD TO GET BEASISWA LIST
    response['beasiswa_list'] = beasiswa_list
    return render(request, '4_info_beasiswa/index.html',response)
