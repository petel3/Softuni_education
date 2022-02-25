from django import forms

from Online_Library.web_app.models import Profile, Book



class CreateBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','description','image','type')
        widgets={
            'description':forms.Textarea(
                attrs={
                    'rows':3,
                }
            )
        }
class EditBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','description','image','type')
        widgets={
            'description':forms.Textarea(
                attrs={
                    'rows':3,
                }
            )
        }
class DeleteBookForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model=Book
        fields= ('title','description','image','type')

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('first_name','last_name','image_url')
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'image_url':'Image URL',
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }
class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        Book.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model=Profile
        fields = ('first_name', 'last_name', 'image_url')