from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from accounts.forms import RegistrationForm


class RegisterView(View):
    template_name = 'accounts/register.html'


    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        return render(request, self.template_name, context={
            'form': RegistrationForm()
        })


    def post(self, request):
        if request.user.is_authenticated:
            logout(request)

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('profile')

        return render(request, self.template_name, context={
            'form': form,
        })
