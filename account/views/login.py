from django.contrib.auth.views import LoginView as _LoginView


class LoginView(_LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
