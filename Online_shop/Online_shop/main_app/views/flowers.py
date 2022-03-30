from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from Online_shop.main_app.forms.flowers import CreateFlowersForm, EditFlowersForm
from Online_shop.main_app.models import Flower


class FlowersView(ListView):
    template_name = 'flowers/flowers.html'
    queryset = Flower.objects.all()
    context_object_name = 'flowers'



class FlowersCreateView(LoginRequiredMixin,CreateView):
    def get(self, request, *args, **kwargs):
        form_class = CreateFlowersForm()
        template_name = 'flowers/flowers_create.html'
        return render(request, template_name, {'form': form_class})

    def post(self, request, *args, **kwargs):
        user = request.user
        flower = request.POST
        image = request.FILES
        print(flower)
        print(user)
        Flower.objects.create(name=flower['name'], quantity=flower['quantity'], type=flower['type']
                              , description=flower['description'], price=flower['price'], image=image['image'],
                              user_key=user)

        template_name = 'flowers'
        return redirect(template_name)


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FlowersDetailsView(LoginRequiredMixin,DetailView):
    model = Flower
    template_name = 'flowers/flowers_details.html'
    context_object_name = 'flowers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user_key == self.request.user

        return context

class FlowersEditView(UpdateView):
    form_class = EditFlowersForm
    template_name = 'flowers/flowers_edit.html'
    queryset = Flower.objects.all()
    success_url = reverse_lazy('flowers')


class FlowersDeleteVies(DeleteView):
    model = Flower
    template_name = 'flowers/flowers_delete.html'
    success_url = reverse_lazy('flowers')
