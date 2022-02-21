from django.urls import path

from Workshop.main_app.views.generic import show_home, show_dashboard
from Workshop.main_app.views.pets import edit_pet, delete_pet, create_pet
from Workshop.main_app.views.photos import show_pet_photo_details, like_pet_photo,create_photo, edit_photo
from Workshop.main_app.views.profile import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
    path('photo/add/', create_photo, name='create photo'),
    path('photo/edit/<int:pk>/', edit_photo, name='edit photo'),

    path('pet/add/', create_pet, name='create pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),
    )


