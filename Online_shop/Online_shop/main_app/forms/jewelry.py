from django import forms

from Online_shop.main_app.models import Jewelry


class CreateJewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = ('name','quantity','materials','description','price','image')


class EditJewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = ('name','quantity','materials','description','price','image')
