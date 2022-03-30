from django.contrib.auth.views import LoginView, PasswordChangeView

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from Online_shop.accounts.forms import CreateProfileForm, EditProfileForm
from Online_shop.accounts.models import Profile
from Online_shop.common.view_mixins import RedirectToDashboard


class UserRegisterView(RedirectToDashboard, CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/../../templates/profile_edit.html'
    success_url = reverse_lazy('index')


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/../../templates/change_password.html'


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/../../templates/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
