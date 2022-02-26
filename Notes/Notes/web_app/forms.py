from django import forms

from Notes.web_app.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url')
        labels = {
            'first_name': "First Name",
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Note.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url')


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'note_image_url')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'note_image_url': 'Link to Image'
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'note_image_url')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'note_image_url': 'Link to Image'
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'note_image_url')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'note_image_url': 'Link to Image'
        }
