from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index), #localhost:8000/app-one > display index string
    path('path-two', views.new), #localhost:8000/app-one/path-two > display new string
    path('redirect', views.create), #localhost:8000/app-one/redirect > redirect to index
    path('<int:num>', views.show), #localhost:8000/app-one/15 > display placeholder blog 15
    path('<int:num>/edit', views.edit), #localhost:8000/app-one/15/edit > display placeholder to edit blog 15
    path('<int:num>/delete', views.destroy), #localhost:8000/app-one/15/delete > redirect to index from blog 15
]
