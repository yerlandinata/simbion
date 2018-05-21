import logging
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView
from simbion_mvc.entity import Donatur, DonaturIndividual, User
from simbion_mvc.services.login import require_guest_method
from simbion_mvc.services.registration import InvalidRegistrationException, register_donatur_individual

class RegisterDonaturIndividualView(TemplateView):

    template_name = '2_register/donatur-individual.html'

    @require_guest_method
    def get(self, request, *args, **kwargs):
        return render(request, RegisterDonaturIndividualView.template_name)

    @require_guest_method
    def post(self, request, *args, **kwargs):
        response = dict()
        try:
            register_donatur_individual(
                DonaturIndividual(
                    Donatur(
                        User(request.POST['username'], request.POST['password'], 'mahasiswa'),
                        request.POST['no_id'],
                        request.POST['email'],
                        request.POST['nama'],
                        request.POST['npwp'],
                        request.POST['alamat'],
                        request.POST['no_telp']
                    ), request.POST['nik']
                )
            )
        except InvalidRegistrationException:
            response['register_error'] = 'Username \'{}\' tidak dapat digunakan'.format(request.POST['username'])
            return render(request, RegisterDonaturIndividualView.template_name, response)
        return redirect(reverse('login'))
