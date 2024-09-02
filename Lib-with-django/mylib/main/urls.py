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
    path("remove/",views.remove,name="books"),

]

