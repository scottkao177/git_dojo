from Quotes.urls import path
from q_app import views

urlpatterns = [
    #login & registration
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

    #dashboard + add quote + add to favorite / unfavorite
    path('success', views.success),
    path('dashboard', views.dashboard),
    path('add/quote', views.add_quote),
    path('favorite/<int:quote_id>', views.favorite_quote),
    path('unfavorite/<int:quote_id>', views.unfavorite_quote),

    #edit description + delete quote
    path('edit/<int:quote_id>', views.edit),
    path('edit/<int:quote_id>/update', views.edit_quote),
    path('delete/<int:quote_id>', views.delete_quote),

    # Quote Poster's Page
    path('poster/<int:quote_id>', views.quote_poster)
]
