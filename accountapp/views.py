from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import UserUpdateForm


class AccountCreateView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('basicapp:basic')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):

    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):

    model = User
    form_class = UserUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('basicapp:basic')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):

    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
