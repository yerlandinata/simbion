import logging
from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from simbion_mvc.services.login import require_guest_method

class RegisterDonaturYayasanView(TemplateView):

    template_name = '2_register/donatur-yayasan.html'

    @require_guest_method
    def get(self, request, *args, **kwargs):
        return render(request, RegisterDonaturYayasanView.template_name)
