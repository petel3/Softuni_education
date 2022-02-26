from django.shortcuts import render, redirect

from Notes.web_app.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm, DeleteProfileForm
from Notes.web_app.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def home_page(request):
    profile = get_profile()
    notes=Note.objects.all()
    if not profile:
        return redirect('create profile')


    context = {
        'profile': profile,
        'notes':notes

    }

    return render(request, 'home-with-profile.html', context)

def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,

    }
    return render(request, 'home-no-profile.html', context)

def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = CreateNoteForm()
    context = {
        'form': form,

    }
    return render(request,'note-create.html',context)


def edit_note(request,pk):
    note=Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = EditNoteForm(instance=note)
    context = {
        'form': form,
        'note':note

    }
    return render(request,'note-edit.html',context)


def delete_note(request,pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
        'note': note

    }
    return render(request,'note-delete.html',context)


def details_note(request,pk):
    note = Note.objects.get(pk=pk)
    context={
        'note':note
    }
    return render(request,'note-details.html',context)


def profile(request):
    profiles=Profile.objects.all()
    notes=Note.objects.count()
    context={
        'profiles':profiles,
        'notes':notes
    }
    return render(request,'profile.html',context)

def delete_profile(request):
    profile=Profile.objects.all()
    if request.method=="POST":
        form=DeleteProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        profile.delete()
        Note.objects.all().delete()
        return redirect('home page')
