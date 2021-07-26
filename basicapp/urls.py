from django.urls import path
from basicapp.views import helloworld

app_name = 'basicapp'

urlpatterns = [
    path('hello/',helloworld,name='basic'),
]