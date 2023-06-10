from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import HouseRegistration, ImageUpload, AddAmenity
from .models import HouseImages, House, Amenity
from django.conf import settings
from landlords.models import AgentAssignment
from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import os

# Create your views here.
def house_reg(request):
    if request.method == "POST":
        form = HouseRegistration(request.POST)
        if form.is_valid():
            house = form.save(commit=False) #saves the form but not commit to the database yet
            return redirect('preview_house', house_id=house.house_id)
    else:
        form = HouseRegistration()
    context = {'form': form}
    return render(request, "register_house.html", context)

class HouseCreateView(CreateView):
    model = House
    fields = '__all__'

class HouseUpdateView(UpdateView):
    model = House
    fields = '__all__'

class HouseDetailView(DetailView):
    model = House

def preview_house(request, house_id):
    house = House.objects.get(house_id=house_id)
    images = HouseImages.objects.filter(house=house)
    return render(request, 'preview_house.html', {'house': house, 'images': images})


def image_list(request):
    images = HouseImages.objects.all()
    return render(request, 'image_list.html', {'images': images})

def add_amenities(request):
    if request.method == 'POST':
        form = AddAmenity(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_amenities')

class UploadView(FormView):
    template_name = 'upload_image.html'
    form_class = ImageUpload
    success_url = '/done/'

    def form_valid(self, form) -> HttpResponse:
        for each in form.cleaned_data['media']:
            HouseImages.objects.create(file=each)
        return super(UploadView, self).form_valid(form)

class AmenitiesView(TemplateView):
    template_name = 'search.html'

class AmenitiesResultsView(ListView):
    model = Amenity
    template_name = 'search1.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Amenity.objects.filter(
            Q(name__icontains=query) | Q(name__icontains=query)
        )
        return object_list

