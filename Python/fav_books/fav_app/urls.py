from fav_books.urls import path
from fav_app import views

urlpatterns = [
    #login & registration
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

    #dashboard + add book + add to favorite / unfavorite
    path('success', views.success_dashboard),
    path('add/book', views.add_book),
    path('favorite/<int:book_id>/book', views.favorite_book),
    path('unfavorite/<int:book_id>/book', views.unfavorite_book),

    #edit description + delete book
    path('edit/<int:book_id>/book', views.edit_book),
    path('delete/<int:book_id>/book', views.delete_book),

    #current book
    path('current/<int:book_id>/book', views.current_book),
]
