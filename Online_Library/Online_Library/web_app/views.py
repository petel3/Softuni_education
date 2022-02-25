from django.shortcuts import render, redirect

# Create your views here.
from Online_Library.web_app.forms import CreateProfileForm, CreateBookForm, EditBookForm, DeleteBookForm, \
    EditProfileForm, DeleteProfileForm
from Online_Library.web_app.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    books = Book.objects.all()
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    context = {
        'profile': profile,
        'books': books
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
        'profile': profile,
    }
    return render(request, 'home-no-profile.html', context)

def profile(request):
    profile = get_profile()

    context = {
    'profile': profile,
    }
    return render(request, 'profile.html', context)

def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:

        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'delete-profile.html', context)


def delete_book(request,pk):
    books = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteBookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteBookForm(instance=books)
        books.delete()
        return redirect('show home')


def add_book(request):
    profile = get_profile()

    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateBookForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('show home')
    else:
        form = EditBookForm(instance=book)
        context = {
            'form': form,
            'book': book,
            'profile':profile
        }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    books = Book.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'books': books,
        'profile': profile
    }
    return render(request, 'book-details.html', context)





def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)
        context = {
            'form': form,
            'profile': profile
        }
    return render(request, 'edit-profile.html',context)

