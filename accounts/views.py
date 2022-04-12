from django.contrib.auth import views as auth_views, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from djangoProject1.accounts.forms import UserRegisterForm, ProfileInformationForm


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_template.html'
    success_url = reverse_lazy('Home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/loginForm.html'
    success_url = reverse_lazy('ProfileSetInfo')

    def form_valid(self,*args,**kwargs):
        result = super().form_valid(*args,**kwargs)

        login(self.request,self.object)
        return result

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class UserLogOutView(auth_views.LogoutView):
    next_page = reverse_lazy('Login')


class ProfileView(TemplateView):
    template_name = 'profile.html'


# @login_required
class ProfileSetInformationView(CreateView):
    form_class = ProfileInformationForm
    template_name = 'accounts/profileInfo.html'
    success_url = reverse_lazy('Home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return  kwargs

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class ProfileEditView(UpdateView):
    form_class = ProfileInformationForm
    template_name = 'accounts/profileInfo.html'
    success_url = reverse_lazy('Profile')

