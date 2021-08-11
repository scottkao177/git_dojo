from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/edit', views.edit),
]