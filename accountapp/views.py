from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render


from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership
from accountapp.forms import UserUpdateForm



has_ownership = [ login_required, account_ownership ]



class AccountCreateView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('basicapp:basic')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):

    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'



@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountUpdateView(UpdateView):

    model = User
    form_class = UserUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('basicapp:basic')
    template_name = 'accountapp/update.html'




@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountDeleteView(DeleteView):

    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
