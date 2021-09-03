from reg_log.urls import path
from reg_log_app import views

urlpatterns = [
    path('', views.index),
    path('main', views.index),
    path('main/register', views.post_register),
    path('main/login', views.post_login),
    path('main/logout', views.post_logout),
    path('main/success', views.success_page),
]
