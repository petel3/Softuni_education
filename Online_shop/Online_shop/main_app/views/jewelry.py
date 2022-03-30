from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from Online_shop.main_app.forms.jewelry import CreateJewelryForm, EditJewelryForm
from Online_shop.main_app.models import Jewelry


class JewelryView(ListView):
    template_name = 'jewelry/jewelry.html'
    queryset = Jewelry.objects.all()
    context_object_name = 'jewels'


class JewelryCreateView(LoginRequiredMixin,CreateView):
    def get(self, request, *args, **kwargs):
        form_class = CreateJewelryForm()
        template_name = 'jewelry/jewelry_create.html'
        return render(request, template_name, {'form': form_class})

    def post(self, request, *args, **kwargs):
        user = request.user
        jewelry = request.POST
        image = request.FILES
        Jewelry.objects.create(name=jewelry['name'], quantity=jewelry['quantity'], materials=jewelry['materials']
                               , description=jewelry['description'], price=jewelry['price'], image=image['image'],
                               user_key=user)
        template_name = 'jewels'
        return redirect(template_name)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JewelryDetailsView(LoginRequiredMixin,DetailView):
    model = Jewelry
    template_name = 'jewelry/jewelry_details.html'
    context_object_name = 'jewels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user_key == self.request.user
        return context

class JewelryEditView(UpdateView):
    form_class = EditJewelryForm
    template_name = 'jewelry/jewelry_edit.html'
    queryset = Jewelry.objects.all()
    success_url = reverse_lazy('jewels')


class JewelryDeleteVies(DeleteView):
    model = Jewelry
    template_name = 'jewelry/jewelry_delete.html'
    success_url = reverse_lazy('jewels')

