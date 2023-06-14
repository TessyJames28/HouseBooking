from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.TenantCreate.as_view(), name='create-tenant'),
    path('dashboard/<str:pk>/', views.dashboard, name="tenant_dashboard"),

]
