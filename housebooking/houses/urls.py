from . import views
from django.contrib import admin
from django.urls import path
from houses.models import Amenity
from django_filters.views import FilterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registration/', views.house_reg, name="house_reg"),
    path('create_house/', views.HouseCreateView.as_view(), name='create-house'),
    path('image_upload/', views.UploadView.as_view(), name="image-upload"), # type: ignore
    path('preview_house/<str:house_id>/', views.preview_house, name="preview_house"),
    path('add_amenities/', views.add_amenities, name='add_amenities'), # type: ignore
    path('search_amenities/', views.AmenitiesResultsView.as_view(), name='amenities'),
    path('amenities_list/', views.AmenitiesView.as_view(), name='amenities_list'),
    path('update_house/<str:pk>/', views.HouseUpdateView.as_view(), name="update-house"),
    path('images/', views.image_list, name='house-images'),
    path('<str:pk>/', views.HouseDetailView.as_view(), name='house-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)