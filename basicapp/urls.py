from django.urls import path
from django.views.generic import TemplateView

from basicapp.views import helloworld

app_name = 'basicapp'

urlpatterns = [
    path('hello/',TemplateView.as_view(template_name='basicapp/basic.html'),name='basic'),
]