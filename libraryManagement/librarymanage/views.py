from os import name
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Author, ToDoList,Item , Book
from .forms import NewBook, search_books , removebook
# Create your views here.
    
def showbyname(request):
    query = request.GET.get('query','')
    books=[]
    author=None

    if query:
        books =Book.objects.filter(title__icontains=query)

        if not books.exists():
            author = Author.objects.filter(name__icontains=query).first()
            return render(request,"librarymanage/list.html",{"author":author})
      
            if author:
                books = author.books.all()
    context={
        'query' : query, 'books' : books, 'author' : author        
    }
    
    return render(request,"librarymanage/book_search.html",context)

def home(response):
    return render(response,"librarymanage/home.html",{})

def authors(response):
    all_auth = Author.objects.all()
    return render(response,"librarymanage/showauthors.html",{"all_auth":all_auth})

def books(response):
    all_books = Book.objects.all()
    return render(response,"librarymanage/showbooks.html",{"all_books":all_books})

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
                return render(response,"librarymanage/errormessage.html",{"message":'This book already exists!'})
            else:
                b = Book(title=t,author=auth,price=p,publication_date=pubdate)
                b.save()
        return HttpResponseRedirect("/books/")
    else:
        form = NewBook()
    return render(response,"librarymanage/create.html",{"newbookform":form})

def remove(response):
    if response.method == "POST":
        form = removebook(response.POST)
        if form.is_valid():
            t = form.cleaned_data["title"]
            b = Book.objects.filter(title=t).first()
            if (b.exists())==False:
                return render(response,"librarymanage/errormessage.html",{"message":'This book does not exist!'})
            else:
                b.delete()
        return HttpResponseRedirect("/books/")
    else:
        form = removebook()
    return render(response,"librarymanage/removeBook.html",{"form":form})
