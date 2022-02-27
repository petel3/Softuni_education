from django.urls import path

from My_music_app.music_app.views import home_page, add_album, album_details, album_edit, album_delete, profile_details, \
    profile_delete, create_profile

urlpatterns =(
    path('',home_page,name='home page'),
    path('album/add',add_album,name='add album'),
    path('album/details/<int:pk>/',album_details,name='album details'),
    path('album/edit/<int:pk>/',album_edit,name='album edit'),
    path('album/delete/<int:pk>/',album_delete,name='album delete'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/',profile_details,name='profile details'),
    path('profile/delete/',profile_delete,name='profile delete'),

)

