from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/dojo', views.dojo),
    path('new/ninja', views.ninja),
]
