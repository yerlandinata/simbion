from django.shortcuts import render
from .login import LoginView, logout
from .register import register, register_donatur, register_donatur_individual, \
                      register_donatur_yayasan, register_mahasiswa
from .register_beasiswa import register_beasiswa
from .give_beasiswa import give_beasiswa
from .wawancara import wawancara
from .pengumuman import pengumuman
from .pembayaran import pembayaran
from .register_skema_beasiswa import register_skema_beasiswa
from .info_beasiswa import info_beasiswa
from .detail_beasiswa import detail_beasiswa

def home(request):
    context = {}
    context['simbion_user'] = request.session.get('simbion_user', False)
    return render(request, 'landing/index.html', context)
