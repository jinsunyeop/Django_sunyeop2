from django.shortcuts import render

from basicapp.models import basic_model


def helloworld(request):
    if request.method == 'POST':
        temp = request.POST.get("input")
        return render(request,'basicapp/basic.html',context={'output':temp})

    else:
        return render(request,'basicapp/basic.html',)