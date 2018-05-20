import logging
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView
from simbion_mvc.services.login import Login, LoginFailedException, attempt_login

class LoginView(TemplateView):

    template_name = '1_login/index.html'

    def get(self, request, *args, **kwargs):
        if request.session.get('simbion_user', False):
            return redirect(reverse('home'))
        return render(request, LoginView.template_name)

    def post(self, request, *args, **kwargs):
        response = dict()
        try:
            user = attempt_login(Login(request.POST['username'], request.POST['password']))
        except LoginFailedException:
            response['login_error'] = True
            return render(request, LoginView.template_name, response)
        request.session['simbion_user'] = user.data
        return redirect(reverse('home'))

def logout(request, *args, **kwargs):
    request.session['simbion_user'] = False
    return redirect(reverse('home'))
