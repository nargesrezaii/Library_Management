from os import name
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Author, Book
from .forms import NewBook, searchbooks , removebook
# Create your views here.

def showbyname(request):
    if request.method == "POST":
        form = searchbooks(request.POST)
        if form.is_valid():
            t = form.cleaned_data["title"]
            b = Book.objects.filter(title=t).first()
            if not b :
                return render(request,"main/errormessage.html",{"message":'This book does not exist!'})
            
            return render(request,"main/bookname.html",{"book":b})
    else:
        form = searchbooks()
    return render(request,"main/book_search.html",{"form":form})

def home(response):
    return render(response,"main/home.html",{})

def authors(response):
    all_auth = Author.objects.all()
    return render(response,"main/showauthors.html",{"all_auth":all_auth})

def books(response):
    all_books = Book.objects.all()
    return render(response,"main/showbooks.html",{"all_books":all_books})

def create(response):
    #save info entered by user in a dictionary.
    if response.method == "POST":
        form = NewBook(response.POST)
        #create new book and author if input is valid
        if form.is_valid():
            t = form.cleaned_data["title"]
            a = form.cleaned_data["author"]
            p = form.cleaned_data["price"]
            pubdate = form.cleaned_data["publication_date"]
            
            if (Author.objects.filter(name=a).exists())==False:
                auth = Author(name=a)
                auth.save()
            else:
                auth = Author.objects.filter(name=a).first()
                
            #check to see if book exists
            if Book.objects.filter(title=t).exists():
                return render(response,"main/errormessage.html",{"message":'This book already exists!'})
            else:
                b = Book(title=t,author=auth,price=p,publication_date=pubdate)
                b.save()
            return HttpResponseRedirect("/books/")
    else:
        form = NewBook()
    return render(response,"main/create.html",{"newbookform":form})

def remove(request):
    if request.method == "POST":
        form = removebook(request.POST)
        if form.is_valid():
            t = form.cleaned_data["title"]
            b = Book.objects.filter(title=t).first()
            if not b :
                return render(request,"main/errormessage.html",{"message":'This book does not exist!'})
            b.delete()
            return HttpResponseRedirect("/books/")
    else:
        form = removebook()
    return render(request,"main/removeBook.html",{"form":form})
