from django.shortcuts import render
from houses.models import House

# Create your views here.

def index(request):
    houses_available = House.objects.filter(status__exact='a')

    context = {
        'houses_available': houses_available,
    }

    return render(request, 'index.html', context=context)