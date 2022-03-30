from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Online_shop.main_app.forms.souvenirs import EditSouvenirsForm, CreateSouvenirsForm
from Online_shop.main_app.models import Souvenir


class SouvenirsView(ListView):
    template_name = 'souvenirs/souvenirs.html'
    queryset = Souvenir.objects.all()
    context_object_name = 'souvenirs'


class SouvenirsCreateView(LoginRequiredMixin,CreateView):
    def get(self, request, *args, **kwargs):
        form_class = CreateSouvenirsForm()
        template_name = 'souvenirs/souvenirs_create.html'
        return render(request, template_name, {'form': form_class})

    def post(self, request, *args, **kwargs):
        user = request.user
        souvenir = request.POST
        image = request.FILES
        Souvenir.objects.create(name=souvenir['name'], quantity=souvenir['quantity'], type=souvenir['type']
                             , description=souvenir['description'], price=souvenir['price'], image=image['image'],
                             user_key=user)
        template_name = 'souvenirs'
        return redirect(template_name)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SouvenirsDetailsView(LoginRequiredMixin,DetailView):
    model = Souvenir
    template_name = 'souvenirs/souvenirs_details.html'
    context_object_name = 'souvenirs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user_key == self.request.user
        return context


class SouvenirsEditView(UpdateView):
    form_class = EditSouvenirsForm
    template_name = 'souvenirs/souvenirs_edit.html'
    queryset = Souvenir.objects.all()
    success_url = reverse_lazy('souvenirs')


class SouvenirsDeleteVies(DeleteView):
    model = Souvenir
    template_name = 'souvenirs/souvenirs_delete.html'
    success_url = reverse_lazy('souvenirs')
