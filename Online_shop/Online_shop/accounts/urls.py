from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from Online_shop.accounts.views import UserLoginView, UserRegisterView, ProfileDetailsView, ChangeUserPasswordView, \
    EditProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout user'),
    path('edit/<int:pk>', EditProfileView.as_view(), name='edit user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),
]
