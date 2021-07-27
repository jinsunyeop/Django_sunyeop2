from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic import CreateView


class AccountCreateView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('basicapp:basic')
    template_name = 'accountapp/create.html'