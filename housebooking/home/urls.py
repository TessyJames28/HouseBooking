from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.CreateUserView.as_view(), name='create-user'), # type: ignore
]
