from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect ,Http404

from .models import Author, Book
from .forms import NewBook, searchbooks , removebook , booktitleform , editbookform , BookFilterForm
from os import name
from turtle import title


def showbyname(request):
    if request.method == "POST":
        form = searchbooks(request.POST)
        if form.is_valid():
            t = form.cleaned_data["title"]
            b = Book.objects.filter(title=t).first()
            a = Author.objects.filter(name=t).first()
            
            if not b and not a:
                return render(request,"main/errormessage.html",{"message":'This book does not exist!'})
            
            if not a:
                return render(request,"main/bookname.html",{"book":b})
            
            if not b:
                return render(request,"main/list.html",{"author":a})
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
    if response.method == "POST":
        form = NewBook(response.POST)
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


def find_book(request):
    title_form = booktitleform()
    book=None
    error_message=None
    
    if request.method == "POST":
        title_form = booktitleform(request.POST)
        if title_form.is_valid():
            title = title_form.cleaned_data['title']
            book = Book.objects.filter(title=title).first()
            if not book :
                error_message='The book does not exist!'
                
    return render(request,"main/find_book.html",{
        "title_form":title_form,
        'book':book,
        'error_message':error_message
        })


def edit_book(request,book_title):
        book = Book.objects.filter(title=book_title).first()
        if not book:
            return render(request,"main/errormessage.html",{"message":'This book does not exist!'})

        if request.method=="POST":
            form= editbookform(request.POST,instance=book) 
            if form.is_valid():
                book.title=form.cleaned_data['title']
                book.author=form.cleaned_data['author']
                book.price=form.cleaned_data['price']
                book.publication_date=form.cleaned_data['publication_date']
                book.save()
                print("book yes edit no")
                return render(request,"main/bookname.html",{"book":book})
            else:
                print("Form errors:",form.errors)
        else:
            form = editbookform(instance=book)

        return render(request,"main/edit_book.html",{
        "form":form,
        'book':book
        })


def filter_list(request):
    form = BookFilterForm(request.GET)
    books = Book.objects.all()

    if form.is_valid():
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')
        pub_date_start = form.cleaned_data.get('pub_date_start')
        pub_date_end = form.cleaned_data.get('pub_date_end')

        if price_min:
            books = books.filter(price__gte=price_min)
        if price_max:
            books = books.filter(price__lte=price_max)
        if pub_date_start:
            books = books.filter(publication_date__gte=pub_date_start)
        if pub_date_end:
            books = books.filter(publication_date__lte=pub_date_end)

    return render(request, 'main/book_list.html', {'books': books, 'form': form})


def delete_book(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    book.delete()
    return redirect('filter_list')