from django.shortcuts import render, redirect
from django.views.generic import CreateView

from Online_shop.main_app.forms.quotations import CreateQuotationsForm
from Online_shop.main_app.models import AskQuotation


class QuotationCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        form_class = CreateQuotationsForm()
        template_name = 'quotations_create.html'
        return render(request, template_name, {'form': form_class})

    def post(self, request, *args, **kwargs):
        user = request.user
        quotation = request.POST
        AskQuotation.objects.create(user_name=quotation['user_name'],
                                    email_to_contact=quotation['email_to_contact'],
                                    description_for_quotation=quotation['description_for_quotation'],
                                    user_key=user)

        return redirect('index')