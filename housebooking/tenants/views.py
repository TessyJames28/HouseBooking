from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tenant
from django.urls import reverse

# Create your views here.

class TenantCreate(CreateView):
    model = Tenant
    fields = ['identification',
              'id_number',
              'DOB',
    ]

class TenantUpdate(UpdateView):
    model = Tenant
    fields = ['identification',
              'id_number',
              'DOB',
    ]

    def form_valid(self, form):
        form.instance.tenant = self.request.user
        return super().form_valid(form)

def dashboard(request, pk):
    return render(request, "dashboard_tenant.html")