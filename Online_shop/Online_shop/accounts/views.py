from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.views.generic import CreateView

from Online_shop.accounts.forms import CreateProfileForm
from Online_shop.common.view_mixins import RedirectToIndexPage


class UserRegisterView(RedirectToIndexPage, CreateView):
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



