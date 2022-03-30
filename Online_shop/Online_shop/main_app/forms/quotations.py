from django import forms

from Online_shop.main_app.models import AskQuotation


class CreateQuotationsForm(forms.ModelForm):
    class Meta:
        model = AskQuotation
        fields = ('user_name','email_to_contact','description_for_quotation')