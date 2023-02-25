from django.shortcuts import render, redirect, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Book, StatusChoice
from webapp.forms import BookForm


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'book_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                        })

    form = BookForm(data=request.POST)

    if not form.is_valid():
        return render(request, 'book_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    else:
        book = Book.objects.create(**form.cleaned_data)
        return redirect('index')


def update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'book_update.html', context={'form': form, 'book': book})

    form = BookForm(instance=book)
    return render(request, 'book_update.html', context={'form': form, 'book': book})


def delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_confirm_delete.html', context={'book': book})


def confirm_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('index')






