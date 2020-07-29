from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as UserModel
from django.shortcuts import render
from django.views import View


class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    login_url = 'login'

    
    def get(self, request):
        user_profile = UserModel.objects.get(pk=request.user.pk)
        user_profile = { 
            'email': user_profile.email,
            'first_name': user_profile.first_name,
            'last_name': user_profile.last_name,
        }

        return render(request, self.template_name, context={
            'user_profile': user_profile,
        })
