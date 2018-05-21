import logging
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView
from simbion_mvc.services.login import Login, LoginFailedException, attempt_login, require_guest_method, require_role

class LoginView(TemplateView):

    template_name = '1_login/index.html'

    @require_guest_method
    def get(self, request, *args, **kwargs):
        context = dict()
        print(request.GET)
        if 'register_success' in request.GET:
            context['register_success'] = True
        return render(request, LoginView.template_name, context)

    @require_guest_method
    def post(self, request, *args, **kwargs):
        response = dict()
        try:
            user = attempt_login(Login(request.POST['username'], request.POST['password']))
        except LoginFailedException:
            response['login_error'] = True
            return render(request, LoginView.template_name, response)
        request.session['simbion_user'] = user.data
        return redirect(reverse('home'))

@require_role(mahasiswa=True, admin=True, donatur=True) # means: any role
def logout(request, *args, **kwargs):
    request.session['simbion_user'] = False
    return redirect(reverse('home'))
