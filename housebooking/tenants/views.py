from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tenant

# Create your views here.

class TenantCreate(CreateView):
    model = Tenant
    fields = '__all__'

class TenantUpdate(UpdateView):
    model = Tenant