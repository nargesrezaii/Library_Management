from django import forms

class NewBook(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(label="Author:",max_length=200)
    price = forms.IntegerField()
    publication_date = forms.DateField(label="Publication date: (yyyy-mm-dd)")
    
class search_books(forms.Form):
    name=forms.CharField(label="Author or book name:",max_length=200)

class removebook(forms.Form):
    title = forms.CharField(max_length=200)