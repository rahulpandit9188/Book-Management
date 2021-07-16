from django.urls import path
from . import views

urlpatterns = [
    path('new-book/', views.new_book),
    path('view-books/', views.view_books),
    path('delete-book/', views.delete_book),
    path('add/', views.add_book),
    path('edit/', views.edit),
    path('edit-book/', views.edit_book),
    path('search-book/',views.search_book),
    path('search/',views.search),
    path('login/',views.userlogin),
    path('logout/',views.userLogout),
    
]
