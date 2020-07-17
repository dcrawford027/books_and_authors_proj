from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def addBook(request):
    newBook = Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')

def bookDetails(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'authors': Author.objects.all(),
    }
    return render(request, 'book_details.html', context)

def appendAuthor(request, book_id):
    appAuthor = Author.objects.get(id=request.POST['other_authors'])
    book = Book.objects.get(id=book_id)
    book.authors.add(appAuthor)
    return redirect("/book_details/" + str(book.id))

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def addAuthor(request):
    newAuthor = Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')

def authorDetails(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'books': Book.objects.all()
    }
    return render(request, 'author_details.html', context)

def appendBook(request, author_id):
    appBook = Book.objects.get(id=request.POST['other_books'])
    author = Author.objects.get(id=author_id)
    author.books.add(appBook)
    return redirect('/author_details/' + str(author_id))