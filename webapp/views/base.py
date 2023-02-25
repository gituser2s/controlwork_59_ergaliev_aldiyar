from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Book
from django.shortcuts import render



def index_view(request: WSGIRequest):
    books = Book.objects.filter(status='active').exclude(is_deleted=True)
    context = {
        'books': books
    }
    return render(request, 'index.html', context=context)
