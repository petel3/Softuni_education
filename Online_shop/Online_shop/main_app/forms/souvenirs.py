from django import forms

from Online_shop.main_app.models import Souvenir


class CreateSouvenirsForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ('name','quantity','type','description','price','image')


class EditSouvenirsForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ('name','quantity','type','description','price','image')
