from django import forms
from .models import Book


class NewBook(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(label="Author:",max_length=200)
    price = forms.IntegerField()
    publication_date = forms.DateField(label="Publication date:",required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    

class searchbooks(forms.Form):
    title=forms.CharField(label="Author or book name:",max_length=200)


class removebook(forms.Form):
    title = forms.CharField(max_length=200)


class booktitleform(forms.Form):
    title = forms.CharField(label='Book title:',max_length=200)


class editbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','price','publication_date']


class BookFilterForm(forms.Form):
    price_min = forms.DecimalField(required=False, decimal_places=2)
    price_max = forms.DecimalField(required=False, decimal_places=2)
    pub_date_start = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    pub_date_end = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    