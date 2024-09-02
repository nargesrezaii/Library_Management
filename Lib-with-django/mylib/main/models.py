from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    price = models.IntegerField()
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title
        
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=200)
    membership_date = models.DateField()
    
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name