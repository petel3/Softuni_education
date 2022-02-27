from django import forms

from My_music_app.music_app.helpers import BootstrapFormMixin
from My_music_app.music_app.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',

                }

            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),

        }


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name','artist', 'genre',  'description', 'image_url', 'price')
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price'
        }
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',

                }

            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'rows': 3
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),

        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist','genre', 'artist', 'description', 'image_url', 'price')
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price'
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('album_name','artist', 'genre',  'description', 'image_url', 'price')
class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        Album.objects.all().delete()
        self.instance.delete()
        return self.instance
    class Meta:
        model=Profile
        fields = ()