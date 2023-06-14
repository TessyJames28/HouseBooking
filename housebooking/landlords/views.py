from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LandLord
from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

class LandLordListView(ListView):
    model = LandLord
    paginate_by = 10

class LandLordDetailView(DetailView):
    model = LandLord

class LandLordCreate(LoginRequiredMixin, CreateView):
    model = LandLord
    fields = ['identification', 'id_number', 'DOB', 'evidence_of_ownership',
              'do_you_own_the_home']

    def form_valid(self, form):
        form.instance.landlord = self.request.user
        return super().form_valid(form)

class LandLordUpdate(UpdateView):
    model = LandLord
    fields = ['identification', 'id_number', 'DOB', 'evidence_of_ownership',
              'do_you_own_the_home']

def dashboard(request, pk):
    return render(request, "dashboard_landlord.html")