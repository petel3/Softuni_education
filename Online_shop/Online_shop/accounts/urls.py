from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from Online_shop.accounts.views import UserLoginView, UserRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout user'),
    path('register/', UserRegisterView.as_view(), name='register'),

]
