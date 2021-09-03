from Registration.urls import path
from login import views

urlpatterns = [
    path('', views.index),
    path('main', views.index),
    path('main/register', views.post_register),
    path('main/login', views.post_login),
    path('main/logout', views.post_logout),
    path('main/success', views.success_page),
]