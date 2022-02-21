from django.shortcuts import render

from Workshop.main_app.helpers import get_profile
from Workshop.main_app.models import PetPhoto



def show_home(request):
    context={
        'hide_additional_nav_items':True,
    }

    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile=get_profile()

    pet_photos=PetPhoto.objects.prefetch_related('tagged_pets')\
        .filter(tagged_pets__user_profile=profile)
    context={
        'pet_photos':pet_photos,
    }
    return render(request, 'dashboard.html', context)
