from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from Online_shop.main_app.forms.plants import CreatePlantsForm, EditPlantsForm
from Online_shop.main_app.models import Plant


class PlantsView(ListView):
    template_name = 'plants/plants.html'
    queryset = Plant.objects.all()
    context_object_name = 'plants'


class PlantsCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        form_class = CreatePlantsForm()
        template_name = 'plants/plants_create.html'
        return render(request, template_name, {'form': form_class})

    def post(self, request, *args, **kwargs):
        user = request.user
        plant = request.POST
        image = request.FILES
        Plant.objects.create(name=plant['name'], quantity=plant['quantity'], type=plant['type']
                              , description=plant['description'], price=plant['price'], image=image['image'],
                              user_key=user)
        template_name = 'plants'
        return redirect(template_name)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantsDetailsView(DetailView):
    model = Plant
    template_name = 'plants/plants_details.html'
    context_object_name = 'plants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user_key == self.request.user
        return context


class PlantsEditView(UpdateView):
    form_class = EditPlantsForm
    template_name = 'plants/plants_edit.html'
    queryset = Plant.objects.all()
    success_url = reverse_lazy('plants')


class PlantsDeleteVies(DeleteView):
    model = Plant
    template_name = 'plants/plants_delete.html'
    success_url = reverse_lazy('plants')
