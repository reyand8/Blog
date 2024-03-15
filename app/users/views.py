from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView, UpdateView
from .forms import RegisterUserForm, LoginUserForm, ProfileUserForm, UserPasswordChangeForm
from django.urls import reverse_lazy


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Register'}
    success_url = reverse_lazy('users:login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        return reverse_lazy('home')


class ProfileUser(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    model = get_user_model()
    template_name =  'users/profile.html'
    extra_context = {
        'title': 'Profile',
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password/password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')