from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.AgentCreate.as_view(), name='create-agent'),
    path('update/<int:pk>/', views.AgentUpdate.as_view(), name='update-agent'), # type: ignore
    path('dashboard/', views.dashboard, name="dashboard"),

]
