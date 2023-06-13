from django.shortcuts import render
from houses.models import House, HouseImages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    houses_available = House.objects.filter(status__exact='a')

    context = {
        'houses_available': houses_available,
    }

    return render(request, 'index.html', context=context)

class CreateUserView(CreateView):
    model = User
    fields = ['first_name',
              'last_name',
              'email',
              'username',
              'password'
    ]