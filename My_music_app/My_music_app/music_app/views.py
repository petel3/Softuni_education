from django.shortcuts import render, redirect

from My_music_app.music_app.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from My_music_app.music_app.models import Album, Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    albums=Album.objects.all()
    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'albums':albums
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    profile = get_profile()
    album=Album.objects.all()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
        'profile': profile,
        'albums':album
    }
    return render(request, 'home-no-profile.html', context)


def add_album(request):
    album = Album.objects.all()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateAlbumForm()
    context = {
        'form': form,

        'albums': album
    }
    return render(request, 'add-album.html', context)


def album_details(request,pk):
    album = Album.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'album': album,
        'profile': profile
    }
    return render(request, 'album-details.html',context)


def album_edit(request,pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
        'album':album


    }
    return render(request, 'edit-album.html',context)


def album_delete(request,pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteAlbumForm(instance=album)
        context = {
            'form': form,
            'album':album
        }

        return render(request, 'delete-album.html', context)



def profile_details(request):
    profile = get_profile()
    album=Album.objects.count()
    context = {
        'album': album,
        'profile': profile
    }
    return render(request, 'profile-details.html',context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile-delete.html',context)
