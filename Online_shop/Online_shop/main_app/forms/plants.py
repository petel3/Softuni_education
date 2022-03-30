from django import forms

from Online_shop.main_app.models import Plant


class CreatePlantsForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('name','quantity','type','description','price','image')


class EditPlantsForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('name','quantity','type','description','price','image')
