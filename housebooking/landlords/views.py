from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LandLord
from django.views.generic import ListView, TemplateView, FormView, DetailView


# Create your views here.

class LandLordListView(ListView):
    model = LandLord
    paginate_by = 10

class LandLordDetailView(DetailView):
    model = LandLord

class LandLordCreate(CreateView):
    model = LandLord
    fields = '__all__'

class LandLordUpdate(UpdateView):
    model = LandLord
    fields = '__all__'