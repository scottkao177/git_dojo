from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('duel', views.duel),
    path('quest', views.quest),
    path('bakuto', views.bakuto),
    path('raid', views.raid),
    path('outcome', views.outcome)
]
