from django import forms

from Online_shop.main_app.models import Flower


class CreateFlowersForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ('name','quantity','type','description','price','image')


class EditFlowersForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ('name','quantity','type','description','price','image')
