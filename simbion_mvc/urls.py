from django.urls import path, reverse
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='home')),
    path('home', views.home, name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('register/mahasiswa', views.RegisterMahasiswaView.as_view(), name='register-mahasiswa'),
    path('register/donatur', views.register_donatur, name='register-donatur'),
    path('register/donatur/individual', views.RegisterDonaturIndividualView.as_view(), name='register-donatur-individual'),
    path('register/donatur/yayasan', views.RegisterDonaturYayasanView.as_view(), name='register-donatur-yayasan'),
    path('beasiswa/<int:id_skema_beasiswa>/<int:id_skema_beasiswa_aktif>/apply', views.register_beasiswa, name='register-beasiswa'),
    path('beasiswa/apply', views.register_beasiswa, name='register-beasiswa-home'),
    path('beasiswa/admin/selection', views.give_beasiswa, name='give-beasiswa'),
    path('beasiswa/admin/add', views.register_skema_beasiswa, name='register-skema-beasiswa'),
    path('beasiswa/wawancara', views.wawancara, name='wawancara'),
    path('beasiswa/', views.info_beasiswa, name='info-beasiswa'),
    path('beasiswa/<int:id_skema_beasiswa>/<int:id_skema_beasiswa_aktif>', views.detail_beasiswa, name='detail-beasiswa'),
    path('pengumuman', views.pengumuman, name='pengumuman'),
    path('beasiswa/pembayaran', views.pengumuman, name='pembayaran'),
    path('beasiswa/beasiswa/baru', views.register_skema_beasiswa, name='daftar-beasiswa-baru'),
]
