import logging
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView
from simbion_mvc.entity import Mahasiswa, User
from simbion_mvc.services.login import require_guest_method
from simbion_mvc.services.registration import InvalidRegistrationException, register_mahasiswa

class RegisterMahasiswaView(TemplateView):

    template_name = '2_register/mahasiswa.html'

    @require_guest_method
    def get(self, request, *args, **kwargs):
        return render(request, RegisterMahasiswaView.template_name)

    @require_guest_method
    def post(self, request, *args, **kwargs):
        response = dict()
        try:
            register_mahasiswa(
                Mahasiswa(
                    User(request.POST['username'], request.POST['password'], 'mahasiswa'),
                    request.POST['npm'],
                    request.POST['email'],
                    request.POST['nama'],
                    request.POST['alamat_tinggal'],
                    request.POST['alamat_domisili'],
                    request.POST['bank'],
                    request.POST['no_rek'],
                    request.POST['nama_pemilik_rek'],
                    request.POST['no_telp']
                )
            )
        except InvalidRegistrationException:
            response['register_error'] = 'Username \'{}\' tidak dapat digunakan'.format(request.POST['username'])
            return render(request, RegisterMahasiswaView.template_name, response)
        return redirect(reverse('login'))
