from django.urls import path
from . import views

#homepage
urlpatterns = [
    path("search/",views.showbyname,name="name"),
    path("create/",views.create,name="create"),
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("authors/",views.authors,name="authors"),
    path("books/",views.books,name="books"),
    path("remove/",views.remove,name="remove"),
    path("edit/",views.find_book,name="find"),
    path("edit/<str:book_title>",views.edit_book,name="edit_book"),
    path("find/",views.find_book,name="find_book"),
    path("filter/",views.filter_list,name="filter_list"),
    path("delete/<int:book_id>",views.delete_book,name="delete_book"),
]

