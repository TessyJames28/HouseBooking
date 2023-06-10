from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LandLord


# Create your views here.

class LandLordCreate(CreateView):
    model = LandLord

class LandLordUpdate(UpdateView):
    model = LandLord