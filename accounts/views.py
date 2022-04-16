from django.contrib.auth import views as auth_views, login, update_session_auth_hash
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from djangoProject1.accounts.forms import UserRegisterForm, ProfileInformationForm, ChangePasswordForm
from djangoProject1.accounts.models import YouCookUserProfile


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/LoginForm.html'
    success_url = reverse_lazy('Home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/registerForm.html'
    success_url = reverse_lazy('ProfileSetInfo')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)

        login(self.request, self.object)
        return result

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogOutView(auth_views.LogoutView):
    next_page = reverse_lazy('Login')


class ProfileView(LoginRequiredMixin,TemplateView,):
    login_url = reverse_lazy('Register')
    template_name = 'accounts/profile.html'



class ProfileSetInformationView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('Register')

    form_class = ProfileInformationForm
    template_name = 'accounts/profileInfo.html'
    success_url = reverse_lazy('Home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileEditView(LoginRequiredMixin,UpdateView,SuccessMessageMixin,):
    login_url = reverse_lazy('Register')

    model = YouCookUserProfile
    template_name  = 'accounts/editProfileInfo.html'
    success_url = reverse_lazy('Home')
    fields = ['first_name','last_name','profile_description','profile_image',]
    success_message = 'Information successfully updated'

    def put(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        return self.post(kwargs)

class ChangePassword(LoginRequiredMixin,TemplateView):

    form_class = ChangePasswordForm

    def get(self, request, *args, **kwargs):

        form = self.form_class(self.request.user)
        return render(request, 'accounts/PaswordChange.html',{'form': form,})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request, 'accounts/profile.html', {'form': form, 'password_changed': True})
        else:
            return render(request, 'accounts/PaswordChange.html', {'form': form, 'password_changed': False})


