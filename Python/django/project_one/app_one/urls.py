from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('<name>', views.hello_name),
    # path('path-two', views.new), 
    # path('redirect', views.create), 
    # path('<int:num>', views.show), 
    # path('<int:num>/edit', views.edit), 
    # path('<int:num>/delete', views.destroy), 
]